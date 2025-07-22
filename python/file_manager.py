import json
from config import PRODUCT_JSON_PATH

def save_product_data(product: dict):
    with open(PRODUCT_JSON_PATH, "w") as f:
        json.dump(product, f, indent=2)
