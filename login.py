import sqlite3
import bcrypt
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/login.kv')


class LoginScreen(Screen):
    def validate_user(self):
        username = self.ids.username.text
        password = self.ids.password.text

        conn = sqlite3.connect("streamsmart.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, password FROM users WHERE email=?", (username,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            user_id, stored_password = user_data
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                print("Login successful!")
                # Redirect based on user ID
                if user_id in (1, 2):
                    self.manager.current = 'admin_dashboard'
                else:
                    self.manager.current = 'user_dashboard'
            else:
                print("Invalid credentials!")
        else:
            print("User not found!")
