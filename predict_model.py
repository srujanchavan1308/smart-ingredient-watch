import sqlite3
import joblib
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')


# Load model + vectorizer
model = joblib.load('harmful_ingredient_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

# NLP Preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = [word.lower() for word in re.findall(r'\w+', text)]
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
    return ' '.join(tokens)

# Connect to DB
def query_database(cleaned_text):
    conn = sqlite3.connect('additives.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM additives WHERE lower(ingredient) = ?", (cleaned_text.lower(),))
    result = cursor.fetchone()
    conn.close()
    return result

# Unified analysis
def analyze_ingredient(raw_text):
    cleaned_text = preprocess(raw_text)

    db_result = query_database(cleaned_text)

    if db_result:
        return {
            "ingredient": db_result[1],
            "alias": db_result[2],
            "side_effects": db_result[3],
            "risk_level": db_result[4],
            "alert_color": "Red" if db_result[5] == 1 else "Green",
            "source": "Database"
        }
    else:
        # Predict with ML
        vec = vectorizer.transform([cleaned_text])
        label = model.predict(vec)[0]
        return {
            "ingredient": raw_text,
            "risk_level": "High" if label == 1 else "Low",
            "side_effects": "Predicted by model",
            "alert_color": "Red" if label == 1 else "Green",
            "source": "Model"
        }
