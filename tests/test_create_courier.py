from os import getenv

import allure
from pytest import mark
from requests import post

from utilities.enums import ApiEndPoints, ResponseCode, ResponseText


class TestCreateCourier:

    @allure.title(test_title="Проверка создания нового курьера")
    @mark.usefixtures("courier_new")
    @mark.parametrize(
        "response_status, response_data",
        [
            (ResponseCode.CREATED.value, ResponseText.OK.value),
            (
                ResponseCode.CONFLICT.value,
                ResponseText.CREATE_EXISTS_COURIER.value,
            ),
        ],
        ids=["New courier registered", "Existing courier not registered"],
    )
    def test_create_courier(
        self, courier_new: dict, response_status: int, response_data: dict
    ) -> None:
        response = post(
            url=f"{getenv('BASE_URL')}{ApiEndPoints.CREATE_COURIER.value}",
            data=courier_new,
        )
        assert response.status_code == response_status
        assert response.json() == response_data

    @allure.title(test_title="Проверка обязательности ключей")
    @mark.parametrize(
        "bad_payload_new_courier, response_status, response_data",
        [
            (
                "login",
                ResponseCode.BAD_REQUEST.value,
                ResponseText.CREATE_BAD_REQUEST.value,
            ),
            (
                "password",
                ResponseCode.BAD_REQUEST.value,
                ResponseText.CREATE_BAD_REQUEST.value,
            ),
        ],
        indirect=["bad_payload_new_courier"],
        ids=["Absence login", "Absence password"],
    )
    def test_required_fields(
        self,
        bad_payload_new_courier: str,
        response_status: int,
        response_data: str,
    ) -> None:
        response = post(
            url=f"{getenv('BASE_URL')}{ApiEndPoints.CREATE_COURIER.value}",
            data=bad_payload_new_courier,
        )
        assert response.status_code == response_status
        assert response.json() == response_data
