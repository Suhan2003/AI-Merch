import os
from dotenv import load_dotenv
load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# API Endpoints
TEXT_MODEL_URL = "https://router.huggingface.co/v1/chat/completions"
IMAGE_MODEL_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"

# Models
TEXT_MODEL = "moonshotai/Kimi-K2-Instruct:novita"

# Folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FOLDER = "sample_outputs"
PRODUCT_IMAGE_PATH = os.path.join(BASE_DIR, OUTPUT_FOLDER, "product.png")
PRODUCT_JSON_PATH = os.path.join(BASE_DIR, OUTPUT_FOLDER, "product.json")
