import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
""")

cursor.execute(
    "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
    (1, "Dev Test", "dev@example.com")
)

conn.commit()
conn.close()
print("Database initialized successfully!")