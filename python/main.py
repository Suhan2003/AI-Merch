import logging
from utils import ensure_folder_exists
from config import OUTPUT_FOLDER
from ai_content_generator import generate_product_idea, generate_product_image
from file_manager import save_product_data

def main():
    ensure_folder_exists(OUTPUT_FOLDER)

    logging.info("Generating product idea...")
    product = generate_product_idea()
    logging.info(f"Product idea generated: {product}")

    logging.info("Generating product image...")
    image_path = generate_product_image(product['title'])
    product["image_path"] = image_path

    save_product_data(product)
    logging.info("Product data saved successfully!")

if __name__ == "__main__":
    main()
