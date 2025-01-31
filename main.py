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
from subscriptions.youtube import YoutubeScreen
from forgot_password import ForgotPasswordScreen
from admin_subscriptions.admin_netflix import AdminNetflixScreen
from admin_subscriptions.netflix_havetoissue_monthly import NetflixHavetoissueMonthly
from admin_subscriptions.netflix_havetoissue_yearly import NetflixHavetoissueYearly
from admin_subscriptions.admin_amazon import AdminAmazonScreen
from admin_subscriptions.amazon_havetoissue_monthly import AmazonHavetoissueMonthly
from admin_subscriptions.amazon_havetoissue_yearly import AmazonHavetoissueYearly
from admin_subscriptions.admin_hotstar import AdminHotstarScreen
from admin_subscriptions.hotstar_havetoissue_monthly import HotstarHavetoissueMonthly
from admin_subscriptions.hotstar_havetoissue_yearly import HotstarHavetoissueYearly
from admin_subscriptions.admin_spotify import AdminSpotifyScreen
from admin_subscriptions.spotify_havetoissue_monthly import SpotifyHavetoissueMonthly
from admin_subscriptions.admin_youtube import AdminYoutubeScreen
from admin_subscriptions.youtube_havetoissue_monthly import YoutubeHavetoissueMonthly



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
        sm.add_widget(YoutubeScreen(name='youtube_screen'))
        sm.add_widget(ForgotPasswordScreen(name='forgot_password'))
        sm.add_widget(AdminNetflixScreen(name='admin_netflix_screen'))
        sm.add_widget(NetflixHavetoissueMonthly(name='netflix_havetoissue_monthly'))
        sm.add_widget(NetflixHavetoissueYearly(name='netflix_havetoissue_yearly'))
        sm.add_widget(AdminAmazonScreen(name='admin_amazon_screen'))
        sm.add_widget(AmazonHavetoissueMonthly(name='amazon_havetoissue_monthly'))
        sm.add_widget(AmazonHavetoissueYearly(name='amazon_havetoissue_yearly'))
        sm.add_widget(AdminHotstarScreen(name='admin_hotstar_screen'))
        sm.add_widget(HotstarHavetoissueMonthly(name='hotstar_havetoissue_monthly'))
        sm.add_widget(HotstarHavetoissueYearly(name='hotstar_havetoissue_yearly'))
        sm.add_widget(AdminSpotifyScreen(name='admin_spotify_screen'))
        sm.add_widget(SpotifyHavetoissueMonthly(name='spotify_havetoissue_monthly'))
        sm.add_widget(AdminYoutubeScreen(name='admin_youtube_screen'))
        sm.add_widget(YoutubeHavetoissueMonthly(name='youtube_havetoissue_monthly'))

        return sm
    
    def forgot_password(self):
        # Switch to the forgot_password screen
        self.root.current = 'forgot_password'

    
if __name__ == '__main__':
    StreamSmartApp().run()