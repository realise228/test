from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def debug_clicks():
    driver = webdriver.Chrome()
    try:
        print("=== Загрузка Click Events страницы ===")
        driver.get("https://practice-automation.com/click-events/")
        time.sleep(3)
        
        print("=== Анализ Click Events ===")
        

        test_buttons = ["btn1", "btn2", "btn3"]
        
        for btn_id in test_buttons:
            try:
                btn = driver.find_element(By.ID, btn_id)
                print(f"Найдена кнопка {btn_id}: '{btn.text}'")
            except Exception as e:
                print(f"Кнопка {btn_id} не найдена: {e}")
        

        for i in range(1, 4):
            try:
                output_elem = driver.find_element(By.ID, f"output{i}")
                print(f"Найден вывод output{i}: '{output_elem.text}'")
            except:
                print(f"Вывод output{i} не найден")
        
        print("\n=== Тестируем клики ===")
        for btn_id in test_buttons:
            try:
                btn = driver.find_element(By.ID, btn_id)
                print(f"Кликаем на {btn_id}...")
                btn.click()
                time.sleep(2)
                

                output_id = f"output{btn_id[-1]}"
                try:
                    output_elem = driver.find_element(By.ID, output_id)
                    print(f"Вывод после клика {output_id}: '{output_elem.text}'")
                except:
                    print(f"Вывод {output_id} не изменился")
                    
            except Exception as e:
                print(f"Ошибка при клике на {btn_id}: {e}")
                
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_clicks()