from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def debug_popups():
    driver = webdriver.Firefox()
    try:
        driver.get("https://practice-automation.com/popups/")
        time.sleep(3)
        
        print("=== Анализ Popups ===")
        
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"Все кнопки button: {len(buttons)}")
        for i, btn in enumerate(buttons):
            btn_id = btn.get_attribute('id')
            btn_text = btn.text
            print(f"button[{i}]: id='{btn_id}', text='{btn_text}'")
        
        outputs = driver.find_elements(By.ID, "output")
        print(f"Элементы с ID 'output': {len(outputs)}")
        for elem in outputs:
            print(f"output: {elem.text}")
        
        test_buttons = ["alert", "confirm", "prompt", "modal"]
        
        for btn_id in test_buttons:
            try:
                btn = driver.find_element(By.ID, btn_id)
                print(f"\nТестируем кнопку {btn_id}: '{btn.text}'")
                btn.click()
                time.sleep(2)
                
                try:
                    alert = driver.switch_to.alert
                    print(f"Найден alert: '{alert.text}'")
                    alert.accept()
                    print("Alert закрыт")
                except:
                    print("Alert не найден")
                    
                output_elems = driver.find_elements(By.ID, "output")
                if output_elems:
                    print(f"Текст вывода: '{output_elems[0].text}'")
                    
            except Exception as e:
                print(f"Ошибка с кнопкой {btn_id}: {e}")
                
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_popups()