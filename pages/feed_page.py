import allure
from locators import feed_locators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step("Клик на блок последнего заказа")
    def click_by_last_order(self):
        self.find_and_click_element(feed_locators.LAST_ORDER_BUTTON)

    @allure.step("Получение количества заказов из 'Выполнено за все время'")
    def get_information_from_counter(self):
        return self.find_element(feed_locators.COUNTER_ALL_ORDERS).text

    @allure.step('Получение количества заказов из "Выполнено за сегодня"')
    def get_information_from_today_counter(self):
        return self.find_element(feed_locators.COUNTER_TODAY_ORDERS).text

    @allure.step('Клик на кнопку "Конструктор"')
    def click_by_builder_button(self):
        self.find_and_click_element(feed_locators.BUTTON_BUILDER)

    @allure.step('Получение текста из модального окна')
    def get_text_from_window_with_order_details(self):
        return self.find_element(feed_locators.TEXT_WINDOW_WITH_ORDERS).text

    @allure.step('Получение номера заказа в статусе "В работе"')
    def get_number_of_order_from_feed_page(self):
        return self.find_element(feed_locators.ORDER_NUMBER_FROM_FEED_PAGE).text

    @allure.step('Получение времени/номера заказа оформления последнего заказа(Лента заказов)')
    def get_time_last_order_from_feed_page(self):
        return self.find_element(feed_locators.LAST_ORDER).text

