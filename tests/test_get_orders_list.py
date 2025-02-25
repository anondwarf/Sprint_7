import os

import allure
import requests

from utilities.enums import ApiEndPoints
from utilities.helpers import check_exists_key


class TestGetOrdersList:

    @allure.title(test_title="Проверка получения списка заказов")
    def test_get_orders_list(self):
        response = requests.get(
            url=f"{os.getenv('BASE_URL')}{ApiEndPoints.GET_ORDER_LIST.value}"
        )
        assert response.status_code == 200
        assert check_exists_key(response.json(), "orders")
