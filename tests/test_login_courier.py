import os

import pytest
import requests

from utilities.enums import ApiEndPoints, ResponseCode, ResponseText
from utilities.fakers import random_string
from utilities.helpers import check_exists_key, check_string_regexp


class TestLoginCourier:

    @pytest.mark.parametrize(
        "registered_courier, status_code, response_text",
        [
            ("ok", ResponseCode.OK.value, r"^([\s\d]+)$"),
            (
                "login",
                ResponseCode.BAD_REQUEST.value,
                ResponseText.LOGIN_BAD_REQUEST.value,
            ),
            (
                "password",
                ResponseCode.BAD_REQUEST.value,
                ResponseText.LOGIN_BAD_REQUEST.value,
            ),
        ],
        indirect=["registered_courier"],
        ids=["ok", "Absence login", "Absence password"],
    )
    def test_login_courier(
        self,
        registered_courier: dict[str, str],
        status_code: int,
        response_text: str,
    ) -> None:
        response = requests.post(
            url=f"{os.getenv('BASE_URL')}{ApiEndPoints.LOGIN_COURIER.value}",
            data=registered_courier,
        )

        assert response.status_code == status_code

        if response.status_code == ResponseCode.BAD_REQUEST.value:
            assert response.json() == response_text
        else:
            assert check_exists_key(response.json(), "id")
            assert check_string_regexp(
                response_text, str(response.json()["id"])
            )

    @pytest.mark.parametrize(
        "payload, status_code, response_text",
        [
            (
                {"login": random_string(), "password": random_string()},
                ResponseCode.NOT_FOUND.value,
                ResponseText.LOGIN_NOT_FOUND.value,
            )
        ],
        ids=["Non existent courier"],
    )
    def test_not_exists_courier_login(
        self, payload: dict[str, str], status_code: int, response_text: str
    ) -> None:
        response = requests.post(
            url=f"{os.getenv('BASE_URL')}{ApiEndPoints.LOGIN_COURIER.value}",
            data=payload,
        )
        assert response.status_code == status_code
        assert response.json() == response_text
