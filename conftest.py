import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.api_client import APIClient


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
    elif request.param == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site')
    yield driver
    driver.quit()


@pytest.fixture
def register_user_fixture(request):
    user = {}

    def register_user(data):
        nonlocal user
        response = APIClient().create_new_user(endpoint='register', email=data['email'],password=data['password'], name=data['name'])
        user.update({
            "response": response,
            "accessToken": response.json().get('accessToken', '')
        })
        return user

    yield register_user
    request.addfinalizer(lambda: APIClient().delete_user(authorization=user.get("accessToken")))
