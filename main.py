from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from database import initialize_database
from login import LoginScreen
from registration import RegistrationScreen
from user_dashboard import UserDashboardScreen
from admin_dashboard import AdminDashboardScreen


class StreamSmartScreenManager(ScreenManager):
    """Manages the different screens in the Stream Smart app."""
    pass

class StreamSmartApp(App):
    def build(self):
        # Initialize the database (ensure it's idempotent)
        print("Initializing the database...")
        initialize_database()
        
        # Initialize ScreenManager
        sm = StreamSmartScreenManager()
        
        # Add all screens
        print("Adding screens to the app...")
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegistrationScreen(name='registration'))
        sm.add_widget(UserDashboardScreen(name='user_dashboard'))
        sm.add_widget(AdminDashboardScreen(name='admin_dashboard'))
        
        print("App initialized successfully.")
        return sm

    def on_start(self):
        # This method is called when the app starts
        print("Stream Smart App has started.")

    def on_stop(self):
        # This method is called when the app is about to close
        print("Stream Smart App is closing...")

if __name__ == "__main__":
    StreamSmartApp().run()
