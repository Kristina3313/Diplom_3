import allure
import requests


class APIClient:
    def __init__(self):
        pass

    @allure.title('Создание пользователя')
    def create_new_user(self, endpoint, email=None, password=None, name=None):
        url = "https://stellarburgers.nomoreparties.site/api/auth/register"
        data = {"email": email, "password": password, "name": name}
        response = requests.post(url, json=data)
        return response

    @allure.title('Удаление пользователя')
    def delete_user(self, authorization):
        url = "https://stellarburgers.nomoreparties.site/api/auth/user"
        headers = {"Authorization": authorization}
        response = requests.delete(url, headers=headers)
        return response
