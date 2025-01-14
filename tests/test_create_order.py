import os

import allure
import pytest
import requests

from utilities.enums import ApiEndPoints
from utilities.helpers import check_exists_key, check_string_regexp


class TestCreateOrder:

    @allure.title(test_title="Проверка ключа `color` при формировании заказа")
    @pytest.mark.parametrize(
        "generate_order_payloads",
        [
            "black_color",
            "grey_color",
            "both_color",
            "no_color",
            "no_param_color",
        ],
        indirect=["generate_order_payloads"],
        ids=[
            "black_color",
            "grey_color",
            "both_color",
            "no_color",
            "no_param_color",
        ],
    )
    def test_choices_color(self, generate_order_payloads):
        response = requests.post(
            url=f"{os.getenv('BASE_URL')}{ApiEndPoints.CREATE_ORDER.value}",
            data=generate_order_payloads,
        )

        assert response.status_code == 201

        if response.status_code == 201:
            assert check_exists_key(response.json(), "track")
            assert check_string_regexp(
                r"^([\s\d]+)$", str(response.json()["track"])
            )
