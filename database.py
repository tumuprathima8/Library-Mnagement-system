import sqlite3

con = sqlite3.connect("library.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

con.commit()
con.close()

print("Database connected successfully")