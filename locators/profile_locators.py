from selenium.webdriver.common.by import By

# Кнопка "История заказов"
HISTORY_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]")
# Кнопка "Профиль"
PROFILE_BUTTON_IN_PROFILE_PAGE = (By.XPATH, "//a[contains(text(),'Профиль')]")
# Кнопка "Выход"
EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
# Время последнего заказа
LAST_ORDER_FROM_HISTORY = (By.XPATH, "(//li[@class='OrderHistory_listItem__2x95r mb-6'])[last()]")
