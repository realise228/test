import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import os
from datetime import datetime


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    

    try:
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
    except Exception as e:
        pytest.skip(f"Не удалось инициализировать WebDriver: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            try:
                take_screenshot(driver, item.name)
            except Exception as e:
                print(f"Не удалось сделать скриншот: {e}")


def take_screenshot(driver, test_name):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        
        allure.attach.file(
            screenshot_path,
            name=f"{test_name}_{timestamp}",
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"Ошибка при создании скриншота: {e}")