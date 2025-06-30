import os
from PIL import Image
import pytesseract


folder_path = r'C:\Users\Admin\Desktop\smart-ingredient-watch\label-img'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')

for filename in os.listdir(folder_path):
    if filename.lower().endswith(image_extensions):
        image_path = os.path.join(folder_path, filename)
        print(f'Processing image: {filename}')
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print('Extracted text:')
        print(text)
        print('-' * 40)
