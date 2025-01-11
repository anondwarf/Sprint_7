import allure
import pytest
import requests

from utilities.fakers import random_string


@allure.step(title="Регистрация нового курьера")
@pytest.fixture(scope="class")
def registered_courier(request) -> dict[str, str]:
    login = random_string()
    password = random_string()

    payload = {
        "login": login,
        "password": password,
    }

    response = requests.post(
        url="https://qa-scooter.praktikum-services.ru/api/v1/courier",
        data=payload,
    )

    assert response.status_code == 201

    if request.param == "login":
        return {"password": password}
    elif request.param == "password":
        return {"login": login}
    else:
        return payload
