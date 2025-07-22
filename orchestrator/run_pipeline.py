import json
from config import PRODUCT_JSON
from python_runner import run_python_generator
from js_runner import run_js_mockup_generator
from php_publisher import send_to_php_publisher
from utils import save_final_output, show_pipeline_summary

def main():
    # Step 1: Run Python Product Generator
    run_python_generator()
    with open(PRODUCT_JSON, "r") as f:
        product_data = json.load(f)

    # Step 2: Run JS Mockup Generator
    mockup_data = run_js_mockup_generator()

    # Step 3: Send data to PHP Publisher
    publisher_data = send_to_php_publisher(mockup_data)

    # Step 4: Save final combined output & show summary
    final_data = save_final_output(product_data, mockup_data, publisher_data)
    show_pipeline_summary(final_data)

if __name__ == "__main__":
    main()
