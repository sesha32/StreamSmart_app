import sqlite3
import bcrypt
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os

# Load the KV file
Builder.load_file("kv/login.kv")

# Check if the image exists (debugging purpose)
print("Image exists:", os.path.exists("assets/loginbg.jpg"))


class LoginScreen(Screen):
    """
    Screen for user login.
    Validates user credentials and redirects to the appropriate dashboard.
    """

    def validate_user(self):
        """
        Validates the username and password entered by the user.
        Redirects to either the user or admin dashboard upon successful validation.
        """
        # Get username and password inputs
        username = self.ids.username.text
        password = self.ids.password.text

        # Connect to the SQLite database
        try:
            conn = sqlite3.connect("streamsmart.db")
            cursor = conn.cursor()

            # Query the user table for the entered username
            cursor.execute("SELECT id, password FROM users WHERE email=?", (username,))
            user_data = cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return
        finally:
            # Always close the database connection
            conn.close()

        # Validate user credentials
        if user_data:
            user_id, stored_password = user_data
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                print("Login successful!")
                # Redirect based on user role
                if user_id in (1, 2):  # Assuming admin IDs are 1 and 2
                    self.manager.current = 'admin_dashboard'
                else:
                    self.manager.current = 'user_dashboard'
            else:
                print("Invalid credentials! Please check your password.")
        else:
            print("User not found! Please register first or check your email.")

    def clear_inputs(self):
        """
        Clears the username and password fields.
        """
        self.ids.username.text = ""
        self.ids.password.text = ""

    def forgot_password(self):
        """
        Handles the "Forgot Password?" hyperlink click.
        """
        print("Forgot Password clicked!")
        # Add functionality to redirect to reset password page or display info.


class MainApp(App):
    def build(self):
        """
        Builds the app and sets up the screen manager.
        """
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(Screen(name='admin_dashboard'))  # Placeholder for Admin Dashboard
        sm.add_widget(Screen(name='user_dashboard'))  # Placeholder for User Dashboard
        return sm

    def forgot_password(self):
        """
        Function called when 'Forgot Password?' is clicked.
        """
        print("Redirecting to Forgot Password page...")
        # You can define further logic here to navigate to a reset password screen or logic.


if __name__ == '__main__':
    MainApp().run()
