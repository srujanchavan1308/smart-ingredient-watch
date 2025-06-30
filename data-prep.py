
import pandas as pd

file_path = "C:\\Users\\Admin\\Desktop\\smart-ingredient-watch\\additives_50.csv"  
df = pd.read_csv(file_path)


print("Dataset shape:", df.shape)
print(df.head())


df['ingredient_name'] = df['ingredient_name'].str.lower().str.strip()
df['aliases'] = df['aliases'].fillna("").str.lower().str.strip()
df['side_effects'] = df['side_effects'].fillna("None")
df['risk_level'] = df['risk_level'].fillna("Unknown")


print("\nLabel Distribution:")
print(df['label'].value_counts())


df.to_csv("cleaned_ingredient_dataset.csv", index=False)
print("Cleaned dataset saved as 'cleaned_ingredient_dataset.csv'")
