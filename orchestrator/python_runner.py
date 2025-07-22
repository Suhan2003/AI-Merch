import subprocess
from config import PYTHON_MAIN

def run_python_generator():
    print("Running Python Product Generator...")
    subprocess.run(["python", PYTHON_MAIN], check=True)
    print("Product generated successfully!")
