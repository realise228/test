from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def debug_page():
    driver = webdriver.Firefox()
    try:
        driver.get("https://practice-automation.com/form-fields/")
        time.sleep(3)
        
        print("=== Анализ структуры страницы ===")
        
        headers = driver.find_elements(By.TAG_NAME, "h3")
        print(f"Найдено заголовков h3: {len(headers)}")
        for i, header in enumerate(headers):
            print(f"h3[{i}]: {header.text}")
        
        lists = driver.find_elements(By.TAG_NAME, "ul")
        print(f"\nНайдено списков ul: {len(lists)}")
        for i, ul in enumerate(lists):
            items = ul.find_elements(By.TAG_NAME, "li")
            print(f"ul[{i}]: {len(items)} элементов")
            for j, li in enumerate(items):
                print(f"  li[{j}]: {li.text}")
        
        all_li = driver.find_elements(By.TAG_NAME, "li")
        print(f"\nВсего элементов li: {len(all_li)}")
        for i, li in enumerate(all_li):
            print(f"li[{i}]: {li.text}")
            
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_page()