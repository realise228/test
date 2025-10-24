from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def debug_clicks():
    driver = webdriver.Firefox()
    try:
        driver.get("https://practice-automation.com/click-events/")
        time.sleep(3)
        
        print("=== Анализ Click Events ===")
        

        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"Все кнопки button: {len(buttons)}")
        for i, btn in enumerate(buttons):
            btn_id = btn.get_attribute('id')
            btn_text = btn.text
            print(f"button[{i}]: id='{btn_id}', text='{btn_text}'")
        

        outputs = driver.find_elements(By.ID, "output")
        print(f"Элементы с ID 'output': {len(outputs)}")
        

        for i in range(1, 4):
            output_elements = driver.find_elements(By.ID, f"output{i}")
            print(f"Элементы с ID 'output{i}': {len(output_elements)}")
            for elem in output_elements:
                print(f"output{i}: {elem.text}")
        

        print("\n=== Тестируем клики ===")
        test_buttons = [
            ("btn1", "Press Me"),
            ("btn2", "Don't Press Me"), 
            ("btn3", "Button 3")
        ]
        
        for btn_id, expected_text in test_buttons:
            try:
                btn = driver.find_element(By.ID, btn_id)
                print(f"Найдена кнопка {btn_id}: '{btn.text}'")
                btn.click()
                time.sleep(1)
                

                output_id = f"output{btn_id[-1]}"
                output_elem = driver.find_elements(By.ID, output_id)
                if output_elem:
                    print(f"Вывод {output_id}: '{output_elem[0].text}'")
                else:
                    print(f"Вывод {output_id} не найден")
                    
            except Exception as e:
                print(f"Ошибка с кнопкой {btn_id}: {e}")
                
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_clicks()