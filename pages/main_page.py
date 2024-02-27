import time
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators import main_locators
from locators.constants import LOGIN_PAGE_URL
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.find_and_click_element(main_locators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик на текст "Восстановить пароль"')
    def click_text_forgot_password(self):
        self.find_and_click_element(main_locators.TEXT_RECOVERY)

    @allure.step('Ввод email')
    def enter_email_in_login_page(self, email):
        email_field = main_locators.EMAIL_FILED
        WebDriverWait(self.driver, 5).until(EC.url_contains(LOGIN_PAGE_URL))
        self.find_and_click_element(email_field).send_keys(email)

    @allure.step('Ввод пароля')
    def enter_password_in_login_page(self, password):
        password_filed = main_locators.PASSWORD_FILED
        WebDriverWait(self.driver, 5).until(EC.url_contains(LOGIN_PAGE_URL))
        self.find_and_click_element(password_filed).send_keys(password)

    @allure.step('Клик на кнопку "Войти"')
    def click_enter_button(self):
        self.find_and_click_element(main_locators.ENTER_BUTTON)

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_profile_button(self):
        self.find_and_click_element(main_locators.PROFILE_BUTTON)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_by_create_order_button(self):
        self.find_and_click_element(main_locators.CREATE_ORDER_BUTTON)

    @allure.step('Закрытие модального окна')
    def click_by_cross_in_modal_window(self):
        self.find_and_click_element(main_locators.CLOSE_WINDOW)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_order_list_button(self):
        self.find_and_click_element(main_locators.ORDER_LIST_BUTTON)

    @allure.step('Добавление булки в заказ')
    def add_bun_in_order(self):
        self.drag_and_drop(main_locators.CRATOR_BUN, main_locators.ADD_INGREDIENT_IN_ORDER)

    @allure.step('Получение номера заказа')
    def get_number_order_from_window(self):
        locator = main_locators.ORDER_NUMBER
        initial_text = self.find_element(locator).text
        self.wait_for_text_to_change_in_element(locator, initial_text)
        time.sleep(2)
        return self.find_element(locator).text

    @allure.step('Клик на кнопку "Конструктор"')
    def click_to_construktor_button(self):
        self.find_and_click_element(main_locators.CONSTRUKTOR_BUTTON)

    @allure.step('Получение текста с кнопки "Войти в аккаунт"')
    def get_text_from_login_button(self):
        return self.find_element(main_locators.LOGIN_BUTTON).text

    @allure.step('Клик по "Краторная булка"')
    def click_by_crator_bun(self):
        self.find_and_click_element(main_locators.CRATOR_BUN)

    @allure.step('Получение текста со всплывающего окна ингредиентов')
    def get_text_from_ingredient_window(self):
        return self.find_element(main_locators.TEXT_DETAIL_INGREDIENS).text

    @allure.step('Клик по крестику в окне ингрединтов')
    def click_by_cross_in_ingredients_window(self):
        self.find_and_click_element(main_locators.CLOSE_WINDOW)

    @allure.step('Подсчёт количества добавленных булок')
    def count_buns_in_order(self):
        return self.find_element(main_locators.COUNTER_BUN).text

    @allure.step('Получение текста с кнопки "Оформить заказ"')
    def get_text_from_button_autorized_user(self):
        return self.find_element(main_locators.CREATE_ORDER_BUTTON).text

    @allure.step('Добавление булки в заказ')
    def add_bun_r2_d2_in_order(self):
        self.drag_and_drop(main_locators.BUN_R2_D3, main_locators.ADD_INGREDIENT_IN_ORDER)
