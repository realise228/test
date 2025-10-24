from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class ClickEventsPage(BasePage):
    PRESS_ME_BUTTON = (By.ID, "btn1")
    DONT_PRESS_ME_BUTTON = (By.ID, "btn2")
    BUTTON_3 = (By.ID, "btn3")
    
    PRESS_ME_OUTPUT = (By.ID, "output1")
    DONT_PRESS_ME_OUTPUT = (By.ID, "output2")
    BUTTON_3_OUTPUT = (By.ID, "output3")

    URL = "https://practice-automation.com/click-events/"

    def __init__(self, driver):
        super().__init__(driver)
        self.open(self.URL)

    @allure.step("Нажать кнопку 'Press Me'")
    def click_press_me(self):
        self.click(self.PRESS_ME_BUTTON)

    @allure.step("Нажать кнопку 'Don't Press Me'")
    def click_dont_press_me(self):
        self.click(self.DONT_PRESS_ME_BUTTON)

    @allure.step("Нажать третью кнопку")
    def click_button_3(self):
        self.click(self.BUTTON_3)

    @allure.step("Получить текст вывода для кнопки 'Press Me'")
    def get_press_me_output(self):
        return self.get_text(self.PRESS_ME_OUTPUT)

    @allure.step("Получить текст вывода для кнопки 'Don't Press Me'")
    def get_dont_press_me_output(self):
        return self.get_text(self.DONT_PRESS_ME_OUTPUT)

    @allure.step("Получить текст вывода для третьей кнопки")
    def get_button_3_output(self):
        return self.get_text(self.BUTTON_3_OUTPUT)