# 🛡️ Smart Ingredient Watchdog

Smart Ingredient Watchdog is an AI-powered tool that helps users identify harmful food additives in packaged products. It allows users to upload product label images or manually enter ingredients. The system uses OCR, NLP, a risk database, and a trained ML model to analyze each ingredient and raise health alerts.

## 🚀 Features

- 📷 Upload label images (uses OCR to extract text)
- ✍️ Manual ingredient entry option
- 🤖 Harmful additive detection using NLP + ML
- 🎯 Color-coded risk alerts (Red: Harmful, Yellow: Unknown, Green: Safe)
- 💊 Ingredient-wise risk details including side effects
- 🌐 Clean and interactive UI using Streamlit


## 📂 Project Structure

smart-ingredient-watch/
├── app.py                  # Streamlit frontend app  
├── training.py             # ML training script  
├── predict_model.py        # Ingredient analysis script using trained model  
├── ocr_to_csv.py           # OCR output to CSV script  
├── harmful_ingredients.csv # Labeled dataset of food additives  
├── requirements.txt        # Python dependencies  
└── .venv/                  # (Optional) Virtual environment  


## 🛠️ Installation & Setup

1. Clone the repository:
git clone [https://github.com/your-username/smart-ingredient-watch.git](https://github.com/your-username/smart-ingredient-watch.git)
cd smart-ingredient-watch

2. Create & activate a virtual environment:
python -m venv .venv
..venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

5. Download NLTK data (only once):
```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

## ▶️ Run the App

```bash
streamlit run app.py

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## 💡 Technologies Used

* Python
* Streamlit – UI frontend
* Tesseract OCR – Image-to-text extraction
* NLTK – Natural language preprocessing
* Scikit-learn – ML model training and prediction
* Pandas – Data handling
* SQLite (optional) – Ingredient database

## 📘 Example Inputs

**Manual input:**

Sodium Benzoate, E250, MSG, Citric Acid

**OCR example:**
Upload a clear image of an ingredient label. The system extracts text and analyzes it.


## 🛡️ Risk Color Guide

| Color     | Risk Level | Meaning                |
| --------- | ---------- | ---------------------- |
| 🟥 Red    | High       | Harmful additive       |
| 🟨 Yellow | Medium     | Unknown or unverified  |
| 🟩 Green  | Low        | Safe/common ingredient |


## 📃 License

This project is licensed under the MIT License.

## 🙋‍♀️ Author

**Srujan Chavan**
GitHub: [https://github.com/srujanchavan1308](https://github.com/srujanchavan1308)

