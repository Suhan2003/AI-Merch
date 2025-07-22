import re
import json
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def extract_json_from_text(text: str) -> dict:
    """Extract JSON block from text or return raw JSON if already clean."""
    match = re.search(r"```json\s*(.*?)```", text, re.DOTALL)
    json_str = match.group(1).strip() if match else text.strip()
    return json.loads(json_str)

def ensure_folder_exists(folder: str):
    os.makedirs(folder, exist_ok=True)
