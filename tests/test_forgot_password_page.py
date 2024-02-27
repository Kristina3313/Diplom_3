import allure
from conftest import driver
from pages.base_page import BasePage
from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage
from locators.constants import MAIN_PAGE_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL


@allure.story('Тестирование функций на странице "Забыл пароль"')
class TestForgotPasswordPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_redirect_from_recovery_password(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.click_text_forgot_password()
        assert driver.current_url == FORGOT_PASSWORD_URL

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_entering_mail_and_click_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.click_text_forgot_password()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.enter_email_filed('crystalkris13@yandex.ru')
        forgot_page.click_recovery_button()
        base_page = BasePage(driver)
        base_page.wait_for_url(RESET_PASSWORD_URL)
        assert driver.current_url == RESET_PASSWORD_URL

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_and_hide_password_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.click_text_forgot_password()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.enter_email_filed('crystalkris13@yandex.ru')
        forgot_page.click_recovery_button()
        forgot_page.click_by_icon_action()
        status = forgot_page.get_button_status()
        assert 'input_status_active' in status
