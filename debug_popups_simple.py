from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def debug_popups():
    driver = webdriver.Chrome()
    try:
        print("=== Загрузка Popups страницы ===")
        driver.get("https://practice-automation.com/popups/")
        time.sleep(3)
        
        print("=== Анализ Popups ===")
        
        try:
            alert = driver.switch_to.alert
            print(f"Закрываем открытый alert: '{alert.text}'")
            alert.dismiss()
        except:
            print("Открытых алертов нет")
        
        test_buttons = ["alert", "confirm", "prompt", "modal"]
        
        for btn_id in test_buttons:
            try:
                btn = driver.find_element(By.ID, btn_id)
                print(f"Найдена кнопка {btn_id}: '{btn.text}'")
            except Exception as e:
                print(f"Кнопка {btn_id} не найдена: {e}")
        
        try:
            output_elem = driver.find_element(By.ID, "output")
            print(f"Найден вывод output: '{output_elem.text}'")
        except:
            print("Вывод output не найден")
        
        print("\n=== Тестируем кнопки по одной ===")
        for btn_id in test_buttons:
            try:
                print(f"\n--- Тестируем {btn_id} ---")
                btn = driver.find_element(By.ID, btn_id)
                btn.click()
                time.sleep(2)
                
                try:
                    alert = driver.switch_to.alert
                    print(f"Появился alert: '{alert.text}'")
                    
                    if btn_id == "prompt":
                        alert.send_keys("Test User")
                        print("Введен текст в prompt")
                    
                    alert.accept()
                    print("Alert принят")
                    time.sleep(1)
                    
                except Exception as e:
                    print(f"Alert не появился или ошибка: {e}")
                
                try:
                    output_elem = driver.find_element(By.ID, "output")
                    print(f"Текст вывода: '{output_elem.text}'")
                except:
                    print("Вывод не изменился")
                    
            except Exception as e:
                print(f"Ошибка при тестировании {btn_id}: {e}")
                
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_popups()