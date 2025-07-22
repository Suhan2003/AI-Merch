import requests
from io import BytesIO
from PIL import Image
from utils import extract_json_from_text
from config import HUGGINGFACE_API_TOKEN, TEXT_MODEL_URL, TEXT_MODEL, IMAGE_MODEL_URL, PRODUCT_IMAGE_PATH

def generate_product_idea() -> dict:
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payload = {
        "messages": [{
            "role": "user",
            "content": (
                "Return ONLY valid JSON (no extra text, no markdown). "
                "The JSON must have keys: 'title', 'description', and 'tags' (array of 5 strings). "
                "Example: {\"title\": \"...\", \"description\": \"...\", \"tags\": [\"..\", \"..\"]}. "
                "Generate a unique and funny t-shirt idea for programmers."
            )
        }],
        "model": TEXT_MODEL
    }

    response = requests.post(TEXT_MODEL_URL, headers=headers, json=payload)
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    return extract_json_from_text(content)

def generate_product_image(prompt: str) -> str:
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payload = {"inputs": f"A funny and creative t-shirt design concept: {prompt}"}

    response = requests.post(IMAGE_MODEL_URL, headers=headers, json=payload)
    response.raise_for_status()

    image = Image.open(BytesIO(response.content))
    image.save(PRODUCT_IMAGE_PATH)
    return PRODUCT_IMAGE_PATH
