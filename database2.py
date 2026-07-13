import sqlite3
con = sqlite3.connect("student.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")
con.commit()
con.close()
print("Database Created Successfully")