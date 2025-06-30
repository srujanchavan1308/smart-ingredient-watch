import pandas as pd
import joblib

# Load saved model and vectorizer
model = joblib.load('harmful_ingredient_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

# Load new ingredients (replace with your actual CSV or list)
new_ingredients = [
    "sodium benzoate",
    "whole wheat flour",
    "xanthan gum",
    "msg",
    "sugar",
    "red 40"
]

# Create DataFrame
df_new = pd.DataFrame(new_ingredients, columns=['corrected_text'])

# Preprocess and vectorize
X_new_vec = vectorizer.transform(df_new['corrected_text'])

# Predict
predictions = model.predict(X_new_vec)
df_new['prediction'] = predictions
df_new['label'] = df_new['prediction'].map({1: 'harmful', 0: 'safe'})

# Display results
print(df_new[['corrected_text', 'label']])

# Save if needed
df_new.to_csv('predictions.csv', index=False)
print("\nPredictions saved to predictions.csv")
