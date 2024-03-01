import allure
from locators import forgot_password_locators
from pages.base_page import BasePage
from locators.constants import RESET_PASSWORD_URL


class ForgotPasswordPage(BasePage):
    @allure.step('Ввод email в поле восстановления пароля')
    def enter_email_filed(self, email):
        self.input_text(forgot_password_locators.EMAIL_FIELD, email)

    @allure.step('Клик на кнопку "Восстановить"')
    def click_recovery_button(self):
        self.find_and_click_element(forgot_password_locators.BUTTON_RECOVERY)

    @allure.step("Клик на кнопку скрыть/пароль")
    def click_by_icon_action(self):
        self.find_and_click_element(forgot_password_locators.ICON_ACTION)

    @allure.step("Получение статуса кнопки скрыть/пароль")
    def get_button_status(self):
        return self.find_element(forgot_password_locators.SHOW_PASSWORD).get_attribute("class")

    @allure.step("Ожидаем загрузки страницы восстановления пароля")
    def wait_loading_reset_url(self):
        self.wait_for_url(RESET_PASSWORD_URL)


