import sqlite3
import bcrypt
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/forgot_password.kv')

class ForgotPasswordScreen(Screen):
    def reset_password(self):
        email = self.ids.email.text.strip()
        new_password = self.ids.new_password.text.strip()
        confirm_password = self.ids.confirm_password.text.strip()

        # Check if all fields are filled
        if not email or not new_password or not confirm_password:
            print("Please fill all fields!")
            return

        # Check if new passwords match
        if new_password != confirm_password:
            print("Passwords do not match!")
            return

        try:
            # Connect to the database
            conn = sqlite3.connect("streamsmart.db")
            cursor = conn.cursor()

            # Fetch user data by email
            cursor.execute("SELECT id, first_name, last_name, email, mobile, password FROM users WHERE email=?", (email,))
            user_data = cursor.fetchone()

            if user_data:
                user_id, first_name, last_name, email, mobile, stored_password = user_data

                # Hash the new password before saving it
                hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

                # Update the password in the database
                cursor.execute("UPDATE users SET password=? WHERE email=?", (hashed_new_password, email))
                conn.commit()

                print("Password updated successfully!")
                self.manager.current = 'login'  # Redirect to login screen after success
            else:
                print("User not found!")

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()
