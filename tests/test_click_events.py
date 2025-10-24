import pytest
import allure
from pages.click_events_page import ClickEventsPage


@allure.feature("События - Click Events")
class TestClickEventsPage:
    @allure.story("Тестирование кнопки 'Press Me'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_press_me_button(self, driver):
        click_page = ClickEventsPage(driver)
        
        with allure.step("Нажать кнопку 'Press Me'"):
            click_page.click_press_me()
        
        with allure.step("Проверить вывод"):
            output = click_page.get_press_me_output()
            assert "pressed" in output.lower() or "clicked" in output.lower()

    @allure.story("Тестирование кнопки 'Don't Press Me'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dont_press_me_button(self, driver):
        click_page = ClickEventsPage(driver)
        
        with allure.step("Нажать кнопку 'Don't Press Me'"):
            click_page.click_dont_press_me()
        
        with allure.step("Проверить вывод"):
            output = click_page.get_dont_press_me_output()
            assert "why" in output.lower() or "pressed" in output.lower()

    @allure.story("Тестирование третьей кнопки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_button_3(self, driver):
        click_page = ClickEventsPage(driver)
        
        with allure.step("Нажать третью кнопку"):
            click_page.click_button_3()
        
        with allure.step("Проверить вывод"):
            output = click_page.get_button_3_output()
            assert output != "" and len(output) > 0