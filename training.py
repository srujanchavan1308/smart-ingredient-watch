import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Step 1: Load labeled data
df = pd.read_csv('labeled_data.csv')

# Step 2: Text and labels
X = df['corrected_text'].astype(str)  # input text
y = df['label'].map({'harmful': 1, 'safe': 0})  # convert labels to binary

# Step 3: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Vectorize text with TF-IDF
vectorizer = TfidfVectorizer(max_features=3000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 5: Train Logistic Regression
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Step 6: Evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 7: Save model and vectorizer
joblib.dump(model, 'harmful_ingredient_model.joblib')
joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')

print("Model and vectorizer saved.")
