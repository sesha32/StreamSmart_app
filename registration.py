import sqlite3
import bcrypt
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/registration.kv')

class RegistrationScreen(Screen):
    def register_user(self):
        first_name = self.ids.first_name.text
        last_name = self.ids.last_name.text
        email = self.ids.email.text
        mobile = self.ids.mobile.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_password.text

        if password != confirm_password:
            print("Passwords do not match!")
            return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            conn = sqlite3.connect("streamsmart.db")
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO users (first_name, last_name, email, mobile, password, subscriptions)
                               VALUES (?, ?, ?, ?, ?, ?)''',
                           (first_name, last_name, email, mobile, hashed_password, 0))
            conn.commit()
            conn.close()
            print("User registered successfully!")
            self.manager.current = 'login'
        except sqlite3.IntegrityError:
            print("This email is already registered!")
