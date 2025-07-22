import requests
from config import PHP_URL

def send_to_php_publisher(mockup_json):
    print("Sending mockup data to PHP Publisher...")
    response = requests.post(PHP_URL, json=mockup_json)
    if response.status_code == 200:
        print("Product published successfully!")
        return response.json()
    else:
        raise Exception(f"Publisher failed: {response.text}")
