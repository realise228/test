from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_basic_navigation():
    """Простой тест для проверки работы Selenium"""
    driver = webdriver.Chrome()
    try:

        print("=== Тестируем Form Fields ===")
        driver.get("https://practice-automation.com/form-fields/")
        time.sleep(2)
        

        message_field = driver.find_element(By.ID, "message")
        submit_button = driver.find_element(By.ID, "submit-btn")
        
        print("✓ Form Fields страница загружена")
        

        print("\n=== Тестируем Click Events ===")
        driver.get("https://practice-automation.com/click-events/")
        time.sleep(2)
        

        buttons_found = []
        for btn_id in ["btn1", "btn2", "btn3"]:
            try:
                btn = driver.find_element(By.ID, btn_id)
                buttons_found.append(btn_id)
                print(f"✓ Кнопка {btn_id} найдена")
            except:
                print(f"✗ Кнопка {btn_id} не найдена")
        

        print("\n=== Тестируем Popups ===")
        driver.get("https://practice-automation.com/popups/")
        time.sleep(2)
        

        try:
            alert = driver.switch_to.alert
            print(f"Закрываем alert: {alert.text}")
            alert.dismiss()
        except:
            print("Алертов нет")
        
        popup_buttons_found = []
        for btn_id in ["alert", "confirm", "prompt", "modal"]:
            try:
                btn = driver.find_element(By.ID, btn_id)
                popup_buttons_found.append(btn_id)
                print(f"✓ Кнопка {btn_id} найдена")
            except:
                print(f"✗ Кнопка {btn_id} не найдена")
        
        print(f"\n=== ИТОГ ===")
        print(f"Form Fields: ✓ Работает")
        print(f"Click Events: Найдено кнопок - {len(buttons_found)}/{3}")
        print(f"Popups: Найдено кнопок - {len(popup_buttons_found)}/{4}")
        
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_basic_navigation()