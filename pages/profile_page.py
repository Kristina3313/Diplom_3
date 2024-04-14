import allure
from locators import profile_locators
from locators.constants import PROFILE_URL
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Клик на кнопку "История заказов"')
    def click_by_history_button(self):
        self.find_and_click_element(profile_locators.HISTORY_BUTTON)

    @allure.step('Клик на кнопку "Выход"')
    def click_by_exit_button(self):
        self.find_and_click_element(profile_locators.EXIT_BUTTON)

    @allure.step('Скролл до последнего заказа')
    def scroll_to_last_order(self):
        self.scroll_into_view(profile_locators.LAST_ORDER_FROM_HISTORY)

    @allure.step('Получение времени оформления последнего заказа(История заказов)')
    def get_time_last_order_from_profile_page(self):
        return self.find_element(profile_locators.LAST_ORDER_FROM_HISTORY).text

    @allure.step("Ожидаем загрузки страницы профиля")
    def wait_loading_profile_url(self):
        self.wait_for_url(PROFILE_URL)
