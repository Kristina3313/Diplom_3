import allure
from conftest import driver, register_user_fixture
from locators.constants import FEED_URL, MAIN_PAGE_URL
from pages.main_page import MainPage
from pages.data import USER_DATA


@allure.story('Тестирование основного функционала')
class TestMainPage:
    @allure.title('Переход по клику на "Лента заказов"')
    def test_redirect_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_order_list_button()
        assert main_page.get_current_url() == FEED_URL

    @allure.title('Переход по клику на "Конструктор"')
    def test_redirect_to_construktor_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_order_list_button()
        main_page.click_to_construktor_button()
        text = main_page.get_text_from_login_button()
        assert text == 'Войти в аккаунт'

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_show_window_after_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_by_crator_bun()
        text = main_page.get_text_from_ingredient_window()
        assert text == "Детали ингредиента"

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_window_after_click_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_by_crator_bun()
        main_page.click_by_cross_in_ingredients_window()
        text = main_page.get_text_from_login_button()
        assert text == 'Войти в аккаунт'

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_increasing_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.add_bun_r2_d2_in_order()
        quantity = main_page.count_buns_in_order()
        assert quantity == '2'

    @allure.title('Залогиненый пользователь может оформить заказ')
    def test_autorized_user_can_create_order(self, driver, register_user_fixture):
        user_data = USER_DATA
        register_user_fixture(user_data)
        main_page = MainPage(driver)
        main_page.go_to_site(MAIN_PAGE_URL)
        main_page.click_button_personal_account()
        main_page.enter_email_in_login_page(user_data['email'])
        main_page.enter_password_in_login_page(user_data['password'])
        main_page.click_enter_button()
        text = main_page.get_text_from_button_autorized_user()
        assert text == 'Оформить заказ'
