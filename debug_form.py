from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def debug_form():
    driver = webdriver.Firefox()
    try:
        driver.get("https://practice-automation.com/form-fields/")
        time.sleep(3)
        
        print("=== Анализ формы ===")
        
        message_fields = driver.find_elements(By.ID, "message")
        print(f"Поля с ID 'message': {len(message_fields)}")
        
        textareas = driver.find_elements(By.TAG_NAME, "textarea")
        print(f"Все textarea: {len(textareas)}")
        for i, ta in enumerate(textareas):
            print(f"textarea[{i}]: id='{ta.get_attribute('id')}', placeholder='{ta.get_attribute('placeholder')}'")
        
        submit_buttons = driver.find_elements(By.ID, "submit-btn")
        print(f"Кнопки с ID 'submit-btn': {len(submit_buttons)}")
        
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"Все кнопки button: {len(buttons)}")
        for i, btn in enumerate(buttons):
            btn_id = btn.get_attribute('id')
            btn_text = btn.text
            btn_type = btn.get_attribute('type')
            print(f"button[{i}]: text='{btn_text}', id='{btn_id}', type='{btn_type}'")
        
        success_elements = driver.find_elements(By.ID, "success-msg")
        print(f"Элементы с ID 'success-msg': {len(success_elements)}")
        
        all_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'success') or contains(text(), 'Success')]")
        print(f"Элементы с текстом 'success': {len(all_elements)}")
        for elem in all_elements:
            print(f"Элемент: {elem.tag_name}, текст: {elem.text}")
            
        print("\n=== Тестируем заполнение формы ===")
        if message_fields:
            message_fields[0].send_keys("Test message")
            print("Заполнили поле message")
        
        submit_button = None
        for btn in buttons:
            if btn.get_attribute('id') == 'submit-btn' and btn.text == 'Submit':
                submit_button = btn
                break
        
        if submit_button:
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(1)
            submit_button.click()
            print("Нажали кнопку Submit")
        else:
            print("Не найдена кнопка Submit")
        
        time.sleep(2)
        

        print("После отправки формы:")
        all_elements_after = driver.find_elements(By.XPATH, "//*[contains(text(), 'success') or contains(text(), 'thank') or contains(text(), 'submitted') or contains(text(), 'Success')]")
        print(f"Найдено элементов с сообщениями: {len(all_elements_after)}")
        for elem in all_elements_after:
            print(f"Элемент после отправки: {elem.tag_name}, текст: {elem.text}")
            

        print("\nПоиск любых изменений:")
        all_p = driver.find_elements(By.TAG_NAME, "p")
        for p in all_p:
            if p.text:
                print(f"p: {p.text}")
                
        all_div = driver.find_elements(By.TAG_NAME, "div")
        for div in all_div:
            if div.text and len(div.text) < 100:
                print(f"div: {div.text}")
            
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_form()