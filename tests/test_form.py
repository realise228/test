import pytest
import allure
import time
from pages.form_page import FormPage
from selenium.webdriver.common.by import By


@allure.feature("Форма - Form Fields")
class TestFormPage:
    @allure.story("Заполнение формы списком инструментов автоматизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_fill_form_with_automation_tools(self, driver):
        form_page = FormPage(driver)
        
        with allure.step("Проверить наличие секции Automation Tools"):
            assert form_page.is_automation_tools_section_present(), "Секция Automation Tools не найдена"
        
        with allure.step("Получить список инструментов автоматизации"):
            tools_list = form_page.get_automation_tools_list()
            allure.attach(str(tools_list), name="Automation Tools List", attachment_type=allure.attachment_type.TEXT)
            assert len(tools_list) > 0, "Список инструментов автоматизации пуст"
            print(f"Инструменты для заполнения: {tools_list}")
        
        with allure.step("Заполнить поле Message списком инструментов"):
            tools_text = form_page.fill_message_with_automation_tools()
            assert tools_text, "Не удалось заполнить поле Message"
            

            actual_text = form_page.driver.find_element(*form_page.MESSAGE_TEXTAREA).get_attribute('value')
            assert actual_text == tools_text, f"Текст в поле не соответствует ожидаемому. Ожидалось: {tools_text}, Получено: {actual_text}"
            print(f"Поле Message заполнено: {actual_text}")
        
        with allure.step("Нажать кнопку Submit"):
            original_url = form_page.driver.current_url
            form_page.click_submit()
            print("Кнопка Submit нажата")
            
        with allure.step("Проверить что форма обработана без ошибок"):
            time.sleep(2)
            

            current_url = form_page.driver.current_url
            assert "form-fields" in current_url, f"Произошло перенаправление с {original_url} на {current_url}"
            

            error_elements = form_page.driver.find_elements(By.XPATH, "//*[contains(text(), 'error') or contains(text(), 'Error')]")
            visible_errors = [elem for elem in error_elements if elem.is_displayed()]
            assert len(visible_errors) == 0, f"Найдены видимые сообщения об ошибках: {[elem.text for elem in visible_errors]}"
            
            print("Форма успешно обработана без ошибок")

    @allure.story("Проверка наличия секции Automation Tools")
    @allure.severity(allure.severity_level.NORMAL)
    def test_automation_tools_section_exists(self, driver):
        form_page = FormPage(driver)
        
        with allure.step("Проверить наличие секции Automation Tools"):
            is_present = form_page.is_automation_tools_section_present()
            assert is_present, "Секция Automation Tools не найдена на странице"
        
        with allure.step("Получить список инструментов автоматизации"):
            tools_list = form_page.get_automation_tools_list()
            allure.attach(str(tools_list), name="Found Automation Tools", attachment_type=allure.attachment_type.TEXT)
            
            assert len(tools_list) > 0, "Список инструментов автоматизации пуст"
            assert len(tools_list) == 5, f"Ожидалось 5 инструментов, найдено {len(tools_list)}"
            
        with allure.step("Проверить содержание списка инструментов"):
            expected_tools = ["Selenium", "Playwright", "Cypress", "Appium", "Katalon Studio"]
            for expected_tool in expected_tools:
                assert any(expected_tool in tool for tool in tools_list), f"Инструмент {expected_tool} не найден в списке"
            
            print(f"Найдены инструменты: {tools_list}")