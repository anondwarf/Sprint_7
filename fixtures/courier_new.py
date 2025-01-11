import allure
import pytest

from utilities.fakers import random_string


@allure.step(title="Генерация тестового курьера")
@pytest.fixture(scope="class")
def courier_new() -> dict[str, str]:
    login = random_string()
    password = random_string()
    first_name = random_string()

    courier = {
        "login": login,
        "password": password,
        "firstName": first_name,
    }

    return courier


@allure.step(title="Генерация тела запроса создания нового курьера")
@pytest.fixture(scope="class")
def bad_payload_new_courier(request) -> dict[str, str]:
    if request.param == "login":
        return {"password": random_string(), "firstName": random_string()}
    elif request.param == "password":
        return {"login": random_string(), "firstName": random_string()}
    else:
        return {"login": random_string(), "password": random_string()}
