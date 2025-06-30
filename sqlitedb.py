import sqlite3

# Step 1: Connect to database (creates file if not exists)
conn = sqlite3.connect("additives.db")
cursor = conn.cursor()

# Step 2: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS additives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT,
    aliases TEXT,
    side_effects TEXT,
    risk_level TEXT,
    label INTEGER
)
""")

# Step 3: Insert sample data
sample_data = [
    ("Monosodium Glutamate", "MSG", "Headaches, allergic reactions", "High", 1),
    ("Sodium Nitrate", "E250", "Potentially carcinogenic", "High", 1),
    ("Aspartame", "", "May cause dizziness, migraines", "Moderate", 1),
    ("Sugar", "", "", "Low", 0),
    ("Salt", "", "", "Low", 0),
    ("Natural Flavors", "", "May include synthetic chemicals", "Moderate", 1),
    ("Citric Acid", "", "", "Low", 0),
    ("Red 40", "Artificial Coloring", "Hyperactivity in children", "High", 1),
    ("Water", "", "", "Low", 0)
]

cursor.executemany("""
INSERT INTO additives (ingredient, aliases, side_effects, risk_level, label)
VALUES (?, ?, ?, ?, ?)
""", sample_data)

# Step 4: Save and close
conn.commit()
conn.close()

print("✅ SQLite database 'additives.db' created and populated.")
