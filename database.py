import sqlite3

def initialize_database():
    try:
        # Connect to the SQLite database (this will create the db if it doesn't exist)
        conn = sqlite3.connect("streamsmart.db")
        cursor = conn.cursor()

        # Create the users table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            mobile TEXT NOT NULL,
                            password TEXT NOT NULL,
                            subscriptions INTEGER DEFAULT 0)''')

        # Create the netflix_subscriptions table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS netflix_subscriptions (
                            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id INTEGER,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            mobile TEXT,
                            plan TEXT,
                            applied_date TEXT)''')
        
        # Create the amazon_subscriptions table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS amazon_subscriptions (
                            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id INTEGER,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            mobile TEXT,
                            plan TEXT,
                            applied_date TEXT)''')
        
        # Create the hotstar_subscriptions table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS hotstar_subscriptions (
                            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id INTEGER,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            mobile TEXT,
                            plan TEXT,
                            applied_date TEXT)''')
        
        # Create the spotify_subscriptions table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS spotify_subscriptions (
                            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id INTEGER,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            mobile TEXT,
                            plan TEXT,
                            applied_date TEXT)''')

        # Commit changes and close the connection
        conn.commit()
        print("Database initialized and tables created (if they didn't exist).")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        conn.close()
