from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from image_button import ImageButton  # Import ImageButton

# Load the User Dashboard KV file
Builder.load_file('kv/user_dashboard.kv')

class UserDashboardScreen(Screen):
    def open_subscription(self, platform):
        print(f"Opening subscription page for {platform}")
        # Logic to handle the subscription can be added here
