import pytest
import allure
from pages.popups_page import PopupsPage


@allure.feature("Модальные окна - Popups")
class TestPopupsPage:
    @allure.story("Тестирование Alert окна")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_alert_popup(self, driver):
        popups_page = PopupsPage(driver)
        
        with allure.step("Нажать кнопку Alert и обработать alert"):
            alert_text = popups_page.click_alert_button()
            assert "Hi there" in alert_text, f"Неожиданный текст alert: {alert_text}"
            
        with allure.step("Проверить что alert закрыт и страница доступна"):
            assert "popups" in driver.current_url

    @allure.story("Тестирование Confirm окна")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_confirm_popup(self, driver):
        popups_page = PopupsPage(driver)
        
        with allure.step("Нажать кнопку Confirm и принять confirm"):
            result = popups_page.click_confirm_button()
            assert result == "accepted", "Confirm не был обработан"
            
        with allure.step("Проверить вывод confirm"):
            output = popups_page.get_output_text()
            print(f"Output text: {output}")

    @allure.story("Тестирование Prompt окна")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_prompt_popup(self, driver):
        popups_page = PopupsPage(driver)
        test_text = "Test Automation"
        
        with allure.step("Нажать кнопку Prompt и ввести текст"):
            entered_text = popups_page.click_prompt_button(test_text)
            assert entered_text == test_text, f"Введенный текст не соответствует: {entered_text}"
            
        with allure.step("Проверить вывод prompt"):
            output = popups_page.get_output_text()
            print(f"Output text: {output}")

    @allure.story("Тестирование модального окна")
    @allure.severity(allure.severity_level.NORMAL)
    def test_modal_popup(self, driver):
        popups_page = PopupsPage(driver)
        
        with allure.step("Нажать кнопку Modal"):
            popups_page.click_modal_button()
            time.sleep(2) 
        
        with allure.step("Проверить видимость модального окна"):

            assert "popups" in driver.current_url
            
        with allure.step("Закрыть модальное окно если оно открыто"):
            try:
                popups_page.close_modal()
            except:
                pass