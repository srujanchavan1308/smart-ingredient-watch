import csv

def load_ocr_csv(file_path):
    lines = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lines.append(row['extracted_text'])
    return lines

def save_corrected_csv(corrected_lines, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['corrected_text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for line in corrected_lines:
            writer.writerow({'corrected_text': line})

def manual_correction(lines):
    corrected = []
    print("Manual correction started. Press Enter to keep original text.")
    for idx, line in enumerate(lines, 1):
        print(f"\nLine {idx}: {line}")
        correction = input("Corrected (or press Enter to keep): ").strip()
        if correction == '':
            corrected.append(line)
        else:
            corrected.append(correction)
    return corrected

if __name__ == "__main__":
    input_file = r"C:\Users\Admin\Desktop\smart-ingredient-watch\label-img\ocr_results.csv"
    output_file = "corrected_text.csv"

    ocr_lines = load_ocr_csv(input_file)
    corrected_lines = manual_correction(ocr_lines)
    save_corrected_csv(corrected_lines, output_file)

    print(f"\nManual correction completed. Corrected text saved to {output_file}")
