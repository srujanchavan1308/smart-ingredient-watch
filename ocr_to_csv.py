
import pandas as pd
from ocr_reader import extract_text_from_images


folder_path = r'C:\Users\Admin\Desktop\smart-ingredient-watch\label-img'


ocr_data = extract_text_from_images(folder_path)

df = pd.DataFrame(ocr_data)
output_file = f"{folder_path}\\ocr_results.csv"
df.to_csv(output_file, index=False)

print(f"\nOCR results saved to: {output_file}")
