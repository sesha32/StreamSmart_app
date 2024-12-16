from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import LoginScreen
from admindashboard import AdminDashboardScreen
from userdashboard import UserDashboardScreen

class StreamSmartApp(App):
    def build(self):
        # Create the ScreenManager and add screens
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))  # Login screen
        sm.add_widget(AdminDashboardScreen(name='admindashboard'))  # Admin dashboard
        sm.add_widget(UserDashboardScreen(name='userdashboard'))  # User dashboard
        return sm

if __name__ == '__main__':
    StreamSmartApp().run()
