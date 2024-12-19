from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import LoginScreen
from registration import RegistrationScreen  # Assuming the class is defined in register.py
from admindashboard import AdminDashboardScreen
from userdashboard import UserDashboardScreen
from contact import ContactScreen  # Adjust this import based on your file structure
from about import AboutScreen
from faqs import FaqsScreen
from support import SupportScreen
from subscriptions.netflix import NetflixScreen
from subscriptions.amazon import AmazonScreen
from subscriptions.hotstar import HotstarScreen
from subscriptions.spotify import SpotifyScreen
from forgot_password import ForgotPasswordScreen
from admin_subscriptions.admin_netflix import AdminNetflixScreen
from admin_subscriptions.netflix_havetoissue_monthly import NetflixHavetoissueMonthly
from admin_subscriptions.netflix_havetoissue_yearly import NetflixHavetoissueYearly
from admin_subscriptions.admin_amazon import AdminAmazonScreen


class StreamSmartApp(App):
    def build(self):
        # Create the ScreenManager and add screens
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))  # Login screen
        sm.add_widget(RegistrationScreen(name="registration"))
        sm.add_widget(AdminDashboardScreen(name='admindashboard'))  # Admin dashboard
        sm.add_widget(UserDashboardScreen(name='userdashboard'))  # User dashboard
        sm.add_widget(AboutScreen(name="about"))  # Add AboutScreen
        sm.add_widget(FaqsScreen(name="faqs"))    # Add FaqsScreen
        sm.add_widget(SupportScreen(name="support"))  # Add SupportScreen
        sm.add_widget(ContactScreen(name='contact'))
        sm.add_widget(NetflixScreen(name='netflix_screen'))
        sm.add_widget(AmazonScreen(name='amazon_screen'))
        sm.add_widget(HotstarScreen(name='hotstar_screen'))
        sm.add_widget(SpotifyScreen(name='spotify_screen'))
        sm.add_widget(ForgotPasswordScreen(name='forgot_password'))
        sm.add_widget(AdminNetflixScreen(name='admin_netflix_screen'))
        sm.add_widget(NetflixHavetoissueMonthly(name='netflix_havetoissue_monthly'))
        sm.add_widget(NetflixHavetoissueYearly(name='netflix_havetoissue_yearly'))
        sm.add_widget(AdminAmazonScreen(name='admin_amazon_screen'))
        return sm
    
    def forgot_password(self):
        # Switch to the forgot_password screen
        self.root.current = 'forgot_password'

    
if __name__ == '__main__':
    StreamSmartApp().run()