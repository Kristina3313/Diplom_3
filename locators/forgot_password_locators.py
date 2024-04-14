from selenium.webdriver.common.by import By

# Кнопка "Восстановить"
BUTTON_RECOVERY = (By.XPATH, "//button[text()='Восстановить']")
# Поле "Email"
EMAIL_FIELD = (By.XPATH, "//label[text()='Email']//following-sibling::input[@name='name']")
# Кнопка "Сохранить"
SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")
# Пароль отображается
SHOW_PASSWORD = (By.XPATH, "//div[contains(@class, 'input_type_text') and contains(@class, 'input_status_active')]")
# Кнопка скрытия и отображения пароля
ICON_ACTION = (By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]")
