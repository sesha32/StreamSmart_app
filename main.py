from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from database import initialize_database
from login import LoginScreen
from registration import RegistrationScreen
from user_dashboard import UserDashboardScreen
from admin_dashboard import AdminDashboardScreen
from image_button import ImageButton

class StreamSmartScreenManager(ScreenManager):
    pass

class StreamSmartApp(App):
    def build(self):
        initialize_database()
        sm = StreamSmartScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegistrationScreen(name='registration'))
        sm.add_widget(UserDashboardScreen(name='user_dashboard'))
        sm.add_widget(AdminDashboardScreen(name='admin_dashboard'))
        return sm

if __name__ == "__main__":
    StreamSmartApp().run()
