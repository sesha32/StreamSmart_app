import sqlite3

def initialize_database():
    conn = sqlite3.connect("streamsmart.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        mobile TEXT NOT NULL,
                        password TEXT NOT NULL,
                        subscriptions INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()
