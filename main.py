from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import LoginScreen
from admindashboard import AdminDashboardScreen
from userdashboard import UserDashboardScreen
from contact import ContactScreen  # Adjust this import based on your file structure
from about import AboutScreen
from faqs import FaqsScreen
from support import SupportScreen


class StreamSmartApp(App):
    def build(self):
        # Create the ScreenManager and add screens
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))  # Login screen
        sm.add_widget(AdminDashboardScreen(name='admindashboard'))  # Admin dashboard
        sm.add_widget(UserDashboardScreen(name='userdashboard'))  # User dashboard
        sm.add_widget(AboutScreen(name="about"))  # Add AboutScreen
        sm.add_widget(FaqsScreen(name="faqs"))    # Add FaqsScreen
        sm.add_widget(SupportScreen(name="support"))  # Add SupportScreen
        sm.add_widget(ContactScreen(name='contact'))

        return sm

if __name__ == '__main__':
    StreamSmartApp().run()