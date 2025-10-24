from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти кликабельный элемент: {locator}")
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Проверить видимость элемента: {locator}")
    def is_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False