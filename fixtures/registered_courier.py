import os

import allure
import pytest
import requests

from utilities.enums import ApiEndPoints
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

    def _generate_test_courier():
        response_create = requests.post(
            url=f"{os.getenv('BASE_URL')}{ApiEndPoints.CREATE_COURIER.value}",
            data=payload,
        )
        assert response_create.status_code == 201
        return payload

    def _delete_test_courier():
        if request.param == "ok":
            response_auth = requests.post(
                url=f"{os.getenv('BASE_URL')}{ApiEndPoints.LOGIN_COURIER.value}",
                data=payload,
            )
            assert response_auth.status_code == 200

            user_id = response_auth.json()["id"]

            response_delete = requests.delete(
                url=f"{os.getenv('BASE_URL')}{ApiEndPoints.DELETE_COURIER.value}/{user_id}",
            )
            assert response_delete.status_code == 200
        else:
            return

    match request.param:
        case "login":
            data = {"password": password}
        case "password":
            data = {"login": login}
        case "ok":
            data = _generate_test_courier()
        case _:
            raise ValueError("Не правильный параметр")

    yield data
    _delete_test_courier()
