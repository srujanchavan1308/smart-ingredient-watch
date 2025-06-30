import pandas as pd

df = pd.read_csv('corrected_text.csv')


harmful_keywords = [
    'sodium nitrate',
    'monosodium glutamate',
    'artificial coloring',
    'sulfites',
    'aspartame',
    'high fructose corn syrup',
    'trans fat',
    'tartrazine',
    'potassium bromate',
    'butylated hydroxytoluene',
    'propyl gallate',
    'benzoates',
    'parabens',
    'bht',
    'bha',
    'acetaldehyde',
    'azodicarbonamide'
]

def label_ingredient(text):
    text_lower = str(text).lower()
    for keyword in harmful_keywords:
        if keyword in text_lower:
            return 'harmful'
    return 'safe'

df['label'] = df['corrected_text'].apply(label_ingredient)

df.to_csv('labeled_data.csv', index=False)

print("Automatic labeling completed. Labeled data saved to 'labeled_data.csv'.")
