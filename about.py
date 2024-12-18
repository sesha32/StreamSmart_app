from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from userdashboard import UserDashboardScreen

# Define AboutScreen class
class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # About Information
        about_label = Label(
            text=( 
                "[b]About Us[/b]\n\n"
                "Access to premium streaming services has become increasingly expensive, "
                "making it difficult for individuals or small households to justify the cost, "
                "especially when multi-device subscription plans are underutilized. Many users end up "
                "paying the full price for services they only partially use, leading to financial inefficiencies "
                "and limited access to high-quality content for cost-conscious consumers.\n\n"
                "Despite the growing demand for affordable solutions, there is a significant gap in platforms "
                "that enable users to share subscriptions securely while ensuring that the process is transparent "
                "and manageable.\n\n"
                "The challenge lies in developing a secure and scalable solution that allows users to form groups "
                "to share subscriptions effectively. These groups can include friends, family, or even strangers from "
                "different areas who are matched based on their preferences and availability. The platform must ensure "
                "equitable cost distribution, manage user accounts and payments efficiently, and provide a seamless "
                "experience for all participants. By addressing these challenges, such a platform could revolutionize "
                "access to premium streaming services, making them more affordable and accessible to a broader audience."
            ),
            markup=True,
            font_size='16sp',
            halign='left',
            valign='top',
            color=(1, 1, 1, 1)
        )
        about_label.bind(size=about_label.setter('text_size'))
        layout.add_widget(about_label)

        # Back Button
        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"center_x": 0.5},
            background_color=(0.87, 0.19, 0.39, 1)
        )
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, *args):
        """Navigate back to the Dashboard screen."""
        self.manager.current = 'userdashboard'  # Switch to dashboard screen

# Define DashboardScreen class
class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Dashboard Information
        dashboard_label = Label(
            text="Welcome to the Dashboard!",
            font_size='24sp',
            halign='center',
            color=(1, 1, 1, 1)
        )
        layout.add_widget(dashboard_label)

        # Go to About Screen Button
        go_to_about_button = Button(
            text="Go to About Screen",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5},
            background_color=(0.19, 0.87, 0.39, 1)
        )
        go_to_about_button.bind(on_release=self.go_to_about)
        layout.add_widget(go_to_about_button)

        self.add_widget(layout)

    def go_to_about(self, *args):
        """Navigate to the About screen."""
        self.manager.current = 'about'  # Switch to about screen

# Main App Class
class MyApp(App):
    def build(self):
        # Create a ScreenManager
        sm = ScreenManager()

        # Add AboutScreen and DashboardScreen to the ScreenManager
        sm.add_widget(UserDashboardScreen(name='userdashboard'))
        sm.add_widget(AboutScreen(name='about'))

        # Set the initial screen to 'dashboard'
        sm.current = 'dashboard'

        return sm

# Run the App
if __name__ == '__main__':
    MyApp().run()
