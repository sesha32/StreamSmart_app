import sqlite3

def delete_all_tables():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("streamsmart.db")
        cursor = conn.cursor()

        # List of tables to be deleted
        tables = [
            "netflix_subscriptions",
            "amazon_subscriptions",
            "hotstar_subscriptions",
            "spotify_subscriptions"
        ]

        # Drop each table if it exists
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
            print(f"The table '{table}' has been deleted successfully.")

        # Commit changes
        conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        conn.close()

# Call the function
delete_all_tables()
