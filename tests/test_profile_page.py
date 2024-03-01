import allure
from conftest import driver, register_user_fixture
from locators.constants import MAIN_PAGE_URL, PROFILE_URL, ORDER_HISTORY_URL, LOGIN_PAGE_URL
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.data import USER_DATA


@allure.story('Тестирование функций на странице "Профиль"')
class TestProfilePage:
    @allure.title('Переход по клику на "Личный кабинет"')
    def test_click_by_profile_page(self, driver, register_user_fixture):
        user_data = USER_DATA
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.wait_loading_login_url()
        main_page.enter_email_in_login_page(user_data['email'])
        main_page.enter_password_in_login_page(user_data['password'])
        main_page.click_enter_button()
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.wait_loading_profile_url()
        assert main_page.get_current_url() == PROFILE_URL

    @allure.title('Переход в раздел "История заказов"')
    def test_click_by_orders_story(self, driver, register_user_fixture):
        user_data = USER_DATA
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.enter_email_in_login_page(user_data["email"])
        main_page.enter_password_in_login_page(user_data["password"])
        main_page.click_enter_button()
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.click_by_history_button()
        assert main_page.get_current_url() == ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта')
    def test_exit_from_account(self, driver, register_user_fixture):
        user_data = USER_DATA
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.enter_email_in_login_page(user_data["email"])
        main_page.enter_password_in_login_page(user_data["password"])
        main_page.click_enter_button()
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.click_by_exit_button()
        main_page.wait_loading_login_url()
        assert main_page.get_current_url() == LOGIN_PAGE_URL
