from dotenv import load_dotenv

load_dotenv()

pytest_plugins = [
    "fixtures.courier_new",
    "fixtures.registered_courier",
    "fixtures.generate_order_payloads",
]
