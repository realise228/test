from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class PopupsPage(BasePage):
    ALERT_BUTTON = (By.ID, "alert")
    CONFIRM_BUTTON = (By.ID, "confirm")
    PROMPT_BUTTON = (By.ID, "prompt")
    MODAL_BUTTON = (By.ID, "modal")
    
    CONFIRM_OUTPUT = (By.ID, "output")
    PROMPT_OUTPUT = (By.ID, "output")
    
    MODAL = (By.ID, "pum_popup_title_1318")
    MODAL_CLOSE = (By.CLASS_NAME, "pum-close")

    URL = "https://practice-automation.com/popups/"

    def __init__(self, driver):
        super().__init__(driver)
        self.open(self.URL)

    @allure.step("Нажать кнопку Alert и обработать alert")
    def click_alert_button(self):
        self.click(self.ALERT_BUTTON)
        time.sleep(1)  
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except:
            return "Alert не найден"

    @allure.step("Нажать кнопку Confirm и обработать confirm")
    def click_confirm_button(self):
        self.click(self.CONFIRM_BUTTON)
        time.sleep(1)  
        try:
            confirm = self.driver.switch_to.alert
            confirm.accept()  
            return "accepted"
        except:
            return "Confirm не найден"

    @allure.step("Нажать кнопку Prompt и обработать prompt")
    def click_prompt_button(self, text="Test User"):
        self.click(self.PROMPT_BUTTON)
        time.sleep(1)  
        try:
            prompt = self.driver.switch_to.alert
            prompt.send_keys(text)
            prompt.accept()
            return text
        except:
            return "Prompt не найден"

    @allure.step("Нажать кнопку Modal")
    def click_modal_button(self):
        self.click(self.MODAL_BUTTON)

    @allure.step("Получить текст вывода")
    def get_output_text(self):
        try:
            return self.get_text(self.CONFIRM_OUTPUT)
        except:
            return ""

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            self.click(self.MODAL_CLOSE)
        except:
            self.driver.execute_script("document.activeElement.blur();")

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_visible(self.MODAL)