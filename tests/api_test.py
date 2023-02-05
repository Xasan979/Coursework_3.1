import allure
import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"  # assuming your API is running on this url
api_keys_names = ["content",
                  "likes_count",
                  "pic",
                  "pk",
                  "poster_avatar",
                  "poster_name",
                  "views_count"]

@allure.description("Проверка запроса http://127.0.0.1:5000/api/posts")
def test_api_1():
    response = requests.get(f"{BASE_URL}/api/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(all(key in item for key in api_keys_names) for item in data)
    print(f" При тестировании {BASE_URL}/api/posts, возвращает статус код  {response.status_code} ,"
          f" данные в виде {type(data)} ,"
          f" у элементов есть нужные ключи {api_keys_names}")

@allure.description("Проверка запроса http://127.0.0.1:5000/api/posts/1")
def test_api_2():
    response = requests.get(f"{BASE_URL}/api/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert all(key in data for key in api_keys_names)

    print(f" При тестировании {BASE_URL}/api/posts/1, возвращает статус код  {response.status_code} ,"
          f" данные в виде {type(data)} ,"
          f" у элементов есть нужные ключи {api_keys_names}")








