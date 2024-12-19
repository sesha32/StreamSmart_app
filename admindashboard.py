from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from session import SessionManager  # Import SessionManager
from image_button import ImageButton  # Import ImageButton

# Load the Admin Dashboard KV file
Builder.load_file('kv/admin_dashboard.kv')


class AdminDashboardScreen(Screen):
    def on_enter(self):
        """Called when the screen is displayed."""
        # Schedule the method to be called after the screen is fully initialized
        Clock.schedule_once(self.load_user_data, 0.1)

    def load_user_data(self, *args):
        """Load user data from the session and redirect if no user is logged in."""
        user_data = SessionManager.get_user()  # Use get_user() instead of get_user_data()
        if user_data:
            print(f"Admin logged in: {user_data}")
            # Check if welcome_label is available before accessing it
            if 'welcome_label' in self.ids:
                self.ids.welcome_label.text = f"Welcome, Admin {user_data['first_name']}!"
        else:
            print("No admin logged in! Redirecting to login screen.")
            if self.manager:  # Ensure self.manager is available
                self.manager.current = 'login'  # Redirect to the login screen

    def logout(self):
        """Clear the email and password fields before navigating to login."""
        # Clear the session when admin logs out
        SessionManager.clear_session()

        # Clear the email and password fields
        login_screen = self.manager.get_screen('login')
        login_screen.ids.username.text = ''
        login_screen.ids.password.text = ''

        # Navigate to the login screen
        self.manager.current = 'login'

    def open_subscription(self, platform):
        """Navigate to the respective admin subscription screen."""
        print(f"Admin opening subscription page for {platform}")
        if self.manager:  # Ensure self.manager is not None
            if platform == 'Netflix':
                self.manager.current = 'admin_netflix_screen'
            elif platform == 'Amazon Prime':
                self.manager.current = 'admin_amazon_screen'
            elif platform == 'Hotstar':
                self.manager.current = 'admin_hotstar_screen'
            elif platform == 'Spotify':
                self.manager.current = 'admin_spotify_screen'
            elif platform == 'YouTube':
                self.manager.current = 'admin_youtube_screen'
