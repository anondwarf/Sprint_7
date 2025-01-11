import allure
import pytest


@allure.step(title="Генерация тела запроса создания заказа")
@pytest.fixture(scope="class")
def generate_order_payloads(request) -> dict:

    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
    }

    if request.param == "both_color":
        payload["color"] = ["BLACK", "GREY"]
        return payload
    elif request.param == "black_color":
        payload["color"] = ["BLACK"]
        return payload
    elif request.param == "grey_color":
        payload["color"] = ["GREY"]
        return payload
    elif request.param == "no_color":
        payload["color"] = []
        return payload
    elif request.param == "no_param_color":
        return payload
    else:
        raise ValueError("Unknown payload type")
