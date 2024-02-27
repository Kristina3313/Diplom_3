from selenium.webdriver.common.by import By

# Кнопка последнего заказа
LAST_ORDER_BUTTON = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/ul[1]/li[1]")
# Статус "Ваш заказ готовится"
CREATE_ORDER_STATUS = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]")
# Счётчик заказов "Выполнено за всё время"
COUNTER_ALL_ORDERS = (By.CSS_SELECTOR, 'div.undefined.mb-15 p.OrderFeed_number__2MbrQ.text.text_type_digits-large')
# Счётчик заказов "Выполнено за сегодня"
COUNTER_TODAY_ORDERS = (By.CSS_SELECTOR, 'p.OrderFeed_number__2MbrQ.text.text_type_digits-large')
# Кнопка "Конструктор"
BUTTON_BUILDER = (By.XPATH, "//p[contains(text(),'Конструктор')]")
# Модальное окно с деталями заказа
TEXT_WINDOW_WITH_ORDERS = (By.XPATH, "//p[contains(text(),'Cостав')]")
# Номер заказа в работе
ORDER_NUMBER_FROM_FEED_PAGE = (By.CSS_SELECTOR, 'li.text.text_type_digits-default.mb-2')
# Время/номер заказа со страницы заказов
LAST_ORDER = (By.XPATH, "//p[@class='text text_type_main-default text_color_inactive'][1]")
