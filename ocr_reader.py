
import os
import re
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_images(folder_path):
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    ocr_results = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extensions):
            image_path = os.path.join(folder_path, filename)
            print(f' Processing: {filename}')
            try:
                img = Image.open(image_path)
                raw_text = pytesseract.image_to_string(img)

                # Basic cleaning
                text = raw_text.strip()
                text = re.sub(r'\s+', ' ', text)
                text = re.sub(r'[^\w\s,.-]', '', text)
                text = text.lower()

                ocr_results.append({
                    "image": filename,
                    "extracted_text": text
                })
            except Exception as e:
                print(f" Failed to process {filename}: {e}")
    
    return ocr_results
