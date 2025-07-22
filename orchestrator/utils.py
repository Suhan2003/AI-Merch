import os, json, webbrowser
from config import FINAL_OUTPUT, SAMPLE_OUTPUTS_DIR, BASE_DIR

def save_final_output(product_data, mockup_data, publisher_data):
    final_data = {
        "product_idea": product_data,
        "mockup_data": mockup_data,
        "publisher_response": publisher_data
    }
    os.makedirs(SAMPLE_OUTPUTS_DIR, exist_ok=True)
    with open(FINAL_OUTPUT, "w") as f:
        json.dump(final_data, f, indent=2)
    print(f"Final pipeline output saved to {FINAL_OUTPUT}")
    return final_data

def show_pipeline_summary(final_data):
    print("\n=================== PIPELINE COMPLETE! ===================")
    print(f"Title: {final_data['product_idea']['title']}")
    print(f"Description: {final_data['product_idea']['description']}")
    print(f"Mockup: {final_data['mockup_data']['mockup_url']}")
    print(f"Fake Product ID: {final_data['publisher_response']['product_id']}")
    print("===============================================================\n")

    # Auto-open the mockup in browser
    mockup_path = os.path.join(BASE_DIR, final_data['mockup_data']['mockup_url'].lstrip("/"))
    webbrowser.open(f"file://{os.path.abspath(mockup_path)}")