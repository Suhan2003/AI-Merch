import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PYTHON_MAIN = os.path.join(BASE_DIR, "python", "main.py")
JS_SERVER = os.path.join(BASE_DIR, "js", "server.js")
PHP_URL = "http://localhost:8000/fake_publisher.php"

PRODUCT_JSON = os.path.join(BASE_DIR, "sample_outputs", "product.json")
PRODUCT_IMAGE = os.path.join(BASE_DIR, "sample_outputs", "product.png")

FINAL_OUTPUT = os.path.join(BASE_DIR, "sample_outputs", "final_product.json")
SAMPLE_OUTPUTS_DIR = os.path.join(BASE_DIR, "sample_outputs")
