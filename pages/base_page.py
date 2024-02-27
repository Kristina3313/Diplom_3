import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на основную страницу')
    def go_to_site(self, url):
        self.driver.get(url)

    def find_and_click_element(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_url(self, expected_url, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url), f'URL did not change to {expected_url}')

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def drag_and_drop(self, source_locator, target_locator):
        source_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(source_locator))
        target_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(target_locator))
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_text_to_change_in_element(self, locator, initial_text, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: self.find_element(locator).text != initial_text)
