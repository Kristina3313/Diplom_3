import allure
from conftest import driver, register_user_fixture
from locators.constants import MAIN_PAGE_URL, PROFILE_URL, ORDER_HISTORY_URL, LOGIN_PAGE_URL
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.story('Тестирование функций на странице "Профиль"')
class TestProfilePage:
    @allure.title('Переход по клику на "Личный кабинет"')
    def test_click_by_profile_page(self, driver, register_user_fixture):
        user_data = {'email': 'crystalkris01@yandex.ru', 'password': '24675Kris', 'name': 'Test User'}
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        base_page = BasePage(driver)
        base_page.wait_for_url(LOGIN_PAGE_URL)
        main_page.enter_email_in_login_page(user_data['email'])
        main_page.enter_password_in_login_page(user_data['password'])
        main_page.click_enter_button()
        main_page.click_profile_button()
        base_page.wait_for_url(PROFILE_URL)
        assert driver.current_url == PROFILE_URL

    @allure.title('Переход в раздел "История заказов"')
    def test_click_by_orders_story(self, driver, register_user_fixture):
        user_data = {'email': 'crystalkris01@yandex.ru', 'password': '24675Kris', 'name': 'Test User'}
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
        assert driver.current_url == ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта')
    def test_exit_from_account(self, driver, register_user_fixture):
        user_data = {'email': 'crystalkris01@yandex.ru', 'password': '24675Kris', 'name': 'Test User'}
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
        base_page = BasePage(driver)
        base_page.wait_for_url(LOGIN_PAGE_URL)
        assert driver.current_url == LOGIN_PAGE_URL
