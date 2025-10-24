from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure
import time


class FormPage(BasePage):
    MESSAGE_TEXTAREA = (By.ID, "message")
    

    AUTOMATION_TOOLS_SECTION = (By.XPATH, "(//ul)[2]")
    TOOL_ITEMS = (By.XPATH, "(//ul)[2]/li")
    
    SUBMIT_BUTTON = (By.ID, "submit-btn")

    URL = "https://practice-automation.com/form-fields/"

    def __init__(self, driver):
        super().__init__(driver)
        self.open(self.URL)
        time.sleep(2)

    @allure.step("Получить список инструментов автоматизации")
    def get_automation_tools_list(self):
        tools = []
        try:
            tool_elements = self.driver.find_elements(*self.TOOL_ITEMS)
            for tool in tool_elements:
                tools.append(tool.text.strip())
        except Exception as e:
            print(f"Ошибка при получении списка инструментов: {e}")
        
        return tools

    @allure.step("Заполнить поле Message списком инструментов автоматизации")
    def fill_message_with_automation_tools(self):
        tools_list = self.get_automation_tools_list()
        tools_text = "\n".join(tools_list)
        

        textarea = self.find_element(self.MESSAGE_TEXTAREA)
        textarea.clear()
        textarea.send_keys(tools_text)
        
        return tools_text

    @allure.step("Нажать кнопку Submit")
    def click_submit(self):
        submit_button = self.find_clickable_element(self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(1)
        submit_button.click()

    @allure.step("Проверить наличие секции Automation Tools")
    def is_automation_tools_section_present(self):
        return self.is_visible(self.AUTOMATION_TOOLS_SECTION)