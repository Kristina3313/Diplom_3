from selenium.webdriver.common.by import By

# Кнопка "Личный кабинет"
BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
# Кнопка "Конструктор"
CONSTRUKTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
# Текст "Восстановить пароль"
TEXT_RECOVERY = (By.XPATH, "//a[@href='/forgot-password']")
# Поле email
EMAIL_FILED = (By.XPATH, "//label[text()='Email']//following-sibling::input[@name='name']")
# Поле пароль
PASSWORD_FILED = (By.XPATH, "//label[text()='Пароль']//following-sibling::input[@name='Пароль']")
# Кнопка "Войти"
ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
# Кнопка "Личный кабинет"
PROFILE_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
# Кнопка "Оформить заказ"
CREATE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
# Кнопка закрытия модального окна с заказами
CLOSE_WINDOW = (By.XPATH, '//*[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
# Кнопка "Лента заказов"
ORDER_LIST_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
# Краторная булка
CRATOR_BUN = (By.XPATH, "//p[contains(text(),'Краторная булка N-200i')]")
# Элемент составления бургера
ADD_INGREDIENT_IN_ORDER = (By.XPATH, "//span[contains(text(),'Перетяните булочку сюда (верх)')]")
# Номер заказа
ORDER_NUMBER = (By.CSS_SELECTOR, ".Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8")
# Кнопка "Войти в аккаунт"
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
# Текст детали ингредиента во всплывающем окне
TEXT_DETAIL_INGREDIENS = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
# Счётчик количества булок R2_D3
COUNTER_BUN = (By.XPATH, './/p[@class = "counter_counter__num__3nue1"]')
# Флюоресцентная булка
BUN_R2_D3 = (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")
