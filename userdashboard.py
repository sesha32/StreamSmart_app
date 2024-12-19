from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from session import SessionManager  # Import the session manager

# Load the User Dashboard KV file
Builder.load_file('kv/user_dashboard.kv')


class UserDashboardScreen(Screen):
    def on_enter(self):
        """Called when the screen is displayed."""
        # Schedule the method to be called after the screen is fully initialized
        Clock.schedule_once(self.load_user_data, 0.1)

    def load_user_data(self, *args):
        """Load user data from the session and redirect if no user is logged in."""
        user_data = SessionManager.get_user()  # Use get_user() instead of get_user_data()
        if user_data:
            print(f"User logged in: {user_data}")
            # Check if welcome_label is available before accessing it
            if 'welcome_label' in self.ids:
                self.ids.welcome_label.text = f"Welcome, {user_data['first_name']}!"
        else:
            print("No user logged in! Redirecting to login screen.")
            if self.manager:  # Ensure self.manager is available
                self.manager.current = 'login'  # Redirect to the login screen

    def open_subscription(self, platform):
        """Navigate to the respective subscription screen."""
        print(f"Opening subscription page for {platform}")
        if self.manager:  # Ensure self.manager is not None
            if platform == 'Netflix':
                self.manager.current = 'netflix_screen'
            elif platform == 'Amazon Prime':
                self.manager.current = 'amazon_screen'
            elif platform == 'Hotstar':
                self.manager.current = 'hotstar_screen'
            elif platform == 'Spotify':
                self.manager.current = 'spotify_screen'
            elif platform == 'YouTube':
                self.manager.current = 'youtube_screen'

