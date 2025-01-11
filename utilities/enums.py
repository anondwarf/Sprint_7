from enum import Enum


class ApiEndPoints(Enum):
    CREATE_COURIER = "/api/v1/courier"
    LOGIN_COURIER = "/api/v1/courier/login"
    GET_ORDER_LIST = "/api/v1/orders"
    CREATE_ORDER = "/api/v1/orders"


class ResponseCode(Enum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409


class ResponseText(Enum):
    OK = {"ok": True}
    CREATE_EXISTS_COURIER = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой.",
    }
    CREATE_BAD_REQUEST = {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи",
    }
    LOGIN_BAD_REQUEST = {
        "code": 400,
        "message": "Недостаточно данных для входа",
    }
    LOGIN_NOT_FOUND = {"code": 404, "message": "Учетная запись не найдена"}
    # GET_ORDER_BAD_REQUEST = "Недостаточно данных для поиска"
    # GET_ORDER_NOT_FOUND = "Заказ не найден"
