import allure
from conftest import driver, register_user_fixture
from locators.constants import MAIN_PAGE_URL
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.story('Тестирование функций на странице "Заказы"')
class TestFeedPage:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_show_details_window(self, driver, register_user_fixture):
        user_data = {'email': 'crystalkris01@yandex.ru', 'password': '24675Kris', 'name': 'Test User'}
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.enter_email_in_login_page(user_data['email'])
        main_page.enter_password_in_login_page(user_data['password'])
        main_page.click_enter_button()
        main_page.click_order_list_button()
        feed_page = FeedPage(driver)
        feed_page.click_by_last_order()
        expected_text = feed_page.get_text_from_window_with_order_details()
        assert "Cостав" in expected_text

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_all_counter_after_create_new_order(self, driver, register_user_fixture):
        user_data = {'email': 'crystalkris01@yandex.ru', 'password': '24675Kris', 'name': 'Test User'}
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.enter_email_in_login_page(user_data['email'])
        main_page.enter_password_in_login_page(user_data['password'])
        main_page.click_enter_button()
        main_page.click_order_list_button()
        feed_page = FeedPage(driver)
        count_orders = int(feed_page.get_information_from_counter())
        feed_page.click_by_builder_button()
        main_page.add_bun_in_order()
        main_page.click_by_create_order_button()
        main_page.click_by_cross_in_modal_window()
        main_page.click_order_list_button()
        new_count_orders = int(feed_page.get_information_from_counter())
        assert new_count_orders == count_orders+1

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_counter_after_create_new_order(self, driver, register_user_fixture):
        user_data = {'email': 'crystalkris01@yandex.ru', 'password': '24675Kris', 'name': 'Test User'}
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.enter_email_in_login_page(user_data['email'])
        main_page.enter_password_in_login_page(user_data['password'])
        main_page.click_enter_button()
        main_page.click_order_list_button()
        feed_page = FeedPage(driver)
        today_orders = int(feed_page.get_information_from_today_counter())
        feed_page.click_by_builder_button()
        main_page.add_bun_in_order()
        main_page.click_by_create_order_button()
        main_page.click_by_cross_in_modal_window()
        main_page.click_order_list_button()
        new_today_orders = int(feed_page.get_information_from_today_counter())
        assert new_today_orders == today_orders+1

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_status_in_progress_after_create_new_order(self, driver, register_user_fixture):
        user_data = {'email': 'crystalkris01@yandex.ru', 'password': '24675Kris', 'name': 'Test User'}
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.enter_email_in_login_page(user_data['email'])
        main_page.enter_password_in_login_page(user_data['password'])
        main_page.click_enter_button()
        main_page.add_bun_in_order()
        main_page.click_by_create_order_button()
        number_of_order = main_page.get_number_order_from_window()
        main_page.click_by_cross_in_modal_window()
        main_page.click_order_list_button()
        feed_page = FeedPage(driver)
        number_from_status = feed_page.get_number_of_order_from_feed_page()
        assert number_of_order in number_from_status

    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_similar_order_history(self, driver, register_user_fixture):
        user_data = {'email': 'crystalkris01@yandex.ru', 'password': '24675Kris', 'name': 'Test User'}
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.enter_email_in_login_page(user_data['email'])
        main_page.enter_password_in_login_page(user_data['password'])
        main_page.click_enter_button()
        main_page.add_bun_in_order()
        main_page.click_by_create_order_button()
        main_page.click_by_cross_in_modal_window()
        main_page.click_order_list_button()
        feed_page = FeedPage(driver)
        time_from_feed_page = feed_page.get_time_last_order_from_feed_page()
        main_page.click_button_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_by_history_button()
        profile_page.scroll_to_last_order()
        time_from_profile_page = profile_page.get_time_last_order_from_profile_page()
        assert time_from_feed_page in time_from_profile_page
