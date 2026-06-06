import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS goals(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    description TEXT,
    status TEXT DEFAULT 'Pending',
    progress INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS activities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    activity_name TEXT,
    duration INTEGER,
    activity_date TEXT
)
""")

cursor.execute("""
INSERT INTO users(fullname,email,password)
VALUES
('Abishek','abishek@gmail.com','123456'),
('John Doe','john@gmail.com','123456'),
('Alice','alice@gmail.com','123456')
""")

conn.commit()
conn.close()

print("Database Created Successfully")