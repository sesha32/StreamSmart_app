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
                            id INTEGER NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            mobile TEXT NOT NULL,
                            plan TEXT NOT NULL,
                            applied_date TEXT NOT NULL,
                            issued TEXT DEFAULT 'no',
                            team_id INTEGER DEFAULT NULL,
                            issued_date TEXT DEFAULT NULL,
                            expire_date TEXT DEFAULT NULL)''')
        
        # Create the amazon_subscriptions table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS amazon_subscriptions (
                            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id INTEGER NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            mobile TEXT NOT NULL,
                            plan TEXT NOT NULL,
                            applied_date TEXT NOT NULL,
                            issued TEXT DEFAULT 'no',
                            team_id INTEGER DEFAULT NULL,
                            issued_date TEXT DEFAULT NULL,
                            expire_date TEXT DEFAULT NULL)''')
        
        # Create the hotstar_subscriptions table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS hotstar_subscriptions (
                            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id INTEGER NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            mobile TEXT NOT NULL,
                            plan TEXT NOT NULL,
                            applied_date TEXT NOT NULL,
                            issued TEXT DEFAULT 'no',
                            team_id INTEGER DEFAULT NULL,
                            issued_date TEXT DEFAULT NULL,
                            expire_date TEXT DEFAULT NULL)''')
        
        # Create the spotify_subscriptions table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS spotify_subscriptions (
                            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id INTEGER NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            mobile TEXT NOT NULL,
                            plan TEXT NOT NULL,
                            applied_date TEXT NOT NULL,
                            issued TEXT DEFAULT 'no',
                            team_id INTEGER DEFAULT NULL,
                            issued_date TEXT DEFAULT NULL,
                            expire_date TEXT DEFAULT NULL)''')
        
        # Create the spotify_subscriptions table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS youtube_subscriptions (
                            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id INTEGER NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            mobile TEXT NOT NULL,
                            plan TEXT NOT NULL,
                            applied_date TEXT NOT NULL,
                            issued TEXT DEFAULT 'no',
                            team_id INTEGER DEFAULT NULL,
                            issued_date TEXT DEFAULT NULL,
                            expire_date TEXT DEFAULT NULL)''')
        
        # Commit changes and close the connection
        conn.commit()
        print("Database initialized and tables created (if they didn't exist).")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        conn.close()
