import subprocess, requests, time
from config import JS_SERVER, PRODUCT_IMAGE

def run_js_mockup_generator():
    print("Running JS Mockup Generator...")

    js_process = subprocess.Popen(["node", JS_SERVER])
    time.sleep(3)

    files = {"product_image": open(PRODUCT_IMAGE, "rb")}
    response = requests.post("http://localhost:3000/upload", files=files)

    js_process.terminate()

    if response.status_code == 200:
        print("Mockup generated successfully!")
        return response.json()
    else:
        raise Exception(f"Mockup generation failed: {response.text}")
