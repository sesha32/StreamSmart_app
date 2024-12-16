from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Color, Line

from contact import ContactScreen

# Store subscription counts
subscription_counts = {
    "Netflix": {"monthly": 0, "yearly": 0},
    "Prime Video": {"monthly": 0, "yearly": 0},
    "Disney Hotstar": {"monthly": 0, "yearly": 0},
    "zee5": {"monthly": 0, "yearly": 0},
}

# Dashboard Screen
class AdminDashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Overall Layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Top Heading
        heading = Label(
            text="Welcome to StreamSmart\n[b][size=24]Your Destination for Affordable Subscriptions[/size][/b]",
            markup=True,
            font_size='20sp',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2)
        )
        layout.add_widget(heading)

        # Navigation Bar BELOW Heading
        nav_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.05), spacing=10, padding=(0, 5))

        buttons = ["Home", "About", "FAQs", "Support", "Contact Us"]
        for btn_text in buttons:
            button = Button(
                text=btn_text,
                background_color=(0.87, 0.19, 0.39, 1),  # Cherry Red Color
                color=(1, 1, 1, 1),
                font_size='12sp',  # Smaller font size
                size_hint=(None, 1),
                width=100  # Fixed width for buttons
            )
            # Navigation logic for Contact Us button
            if btn_text == "Contact Us":
                button.bind(on_release=self.go_to_contact)  # Call the method instead of using lambda
            # Open the chatbot
            nav_bar.add_widget(button)

        layout.add_widget(nav_bar)

        # Grid for OTT Platforms
        grid = GridLayout(cols=2, spacing=20, size_hint=(1, 0.65))

        ott_platforms = {
            "Netflix": "assets/netflix.jpg",
            "Prime Video": "assets/prime.png",
            "Disney Hotstar": "assets/hotstar.jpg",
            "zee5": "assets/zee5.png",
        }

        for platform_name, image_path in ott_platforms.items():
            grid.add_widget(OTTButton(platform_name, image_path, self))

        layout.add_widget(grid)

        # Bottom Navigation Placeholder
        bottom_label = Label(
            text="Select Your Preferred Platform",
            font_size='16sp',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.05)
        )
        layout.add_widget(bottom_label)

        self.add_widget(layout)

    # Method to switch to the Contact screen
    def go_to_contact(self, instance):
        self.manager.current = "contact"

    def open_platform_page(self, platform_name):
        self.manager.current = platform_name.lower().replace(" ", "_")




    def open_platform_page(self, platform_name):
        self.manager.current = platform_name.lower().replace(" ", "_")
class OTTButton(ButtonBehavior, BoxLayout):
    def __init__(self, platform_name, image_path, parent_screen, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        self.platform_name = platform_name
        self.parent_screen = parent_screen

        # Add thin orange border using Line
        with self.canvas.before:
            Color(0.87, 0.19, 0.39, 1)  # Orange color
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

        self.bind(size=self.update_border, pos=self.update_border)

        # Add image widget
        self.image = Image(source=image_path, size_hint=(1, 0.8))
        self.add_widget(self.image)

        # Add label
        self.label = Label(
            text=f"[b]{platform_name}[/b]",
            markup=True,
            font_size='16sp',
            halign='center',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2)
        )
        self.add_widget(self.label)

        self.bind(on_release=lambda instance: self.parent_screen.open_platform_page(platform_name))

    def update_border(self, *args):
        """Update the thin orange border on size/position changes."""
        self.border.rectangle = (self.x, self.y, self.width, self.height)


# OTT Platform Individual Screens
# OTT Platform Individual Screens
class OTTPlatformScreen(Screen):
    def __init__(self, platform_name, **kwargs):
        super().__init__(**kwargs)
        self.platform_name = platform_name

        # Main layout
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        # Platform Heading
        heading = Label(
            text=f"[b][size=24]{platform_name} Subscription Plans[/size][/b]",
            markup=True,
            font_size='20sp',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.1)
        )
        layout.add_widget(heading)

        # Two Horizontal Sections
        section_layout = GridLayout(cols=2, spacing=20, size_hint=(1, 0.7))

        # Section 1: Have to Issue
        have_to_issue_layout = self.create_subscription_section("Have to Issue")
        section_layout.add_widget(have_to_issue_layout)

        # Section 2: Expiring Soon
        expiring_soon_layout = self.create_subscription_section("Expiring Soon")
        section_layout.add_widget(expiring_soon_layout)

        layout.add_widget(section_layout)

        # Back Button
        back_btn = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"center_x": 0.5},
            background_color=(0.8, 0, 0, 1)
        )
        back_btn.bind(on_release=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def create_subscription_section(self, section_title):
        """Create a section layout with a title and buttons."""
        box = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint=(1, 1))

        # Section Title
        title_label = Label(
            text=f"[b][color=#FF0000]{section_title}[/color][/b]",
            markup=True,
            font_size='18sp',
            halign='center',
            size_hint=(1, 0.2)
        )
        box.add_widget(title_label)

        # Buttons: Monthly Plan and Yearly Plan
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.6))

        monthly_btn = Button(
            text="Monthly Plan",
            size_hint=(0.4, None),  # Reduce width and disable height scaling
            height=40,  # Set fixed height
            background_color=(0.8, 0, 0, 1),
            color=(1, 1, 1, 1)
        )
        monthly_btn.bind(on_release=lambda instance: self.show_subscription_popup("Monthly"))

        yearly_btn = Button(
            text="Yearly Plan",
            size_hint=(0.4, None),  # Reduce width and disable height scaling
            height=40,  # Set fixed height
            background_color=(0.8, 0, 0, 1),
            color=(1, 1, 1, 1)
        )
        yearly_btn.bind(on_release=lambda instance: self.show_subscription_popup("Yearly"))

        button_layout.add_widget(monthly_btn)
        button_layout.add_widget(yearly_btn)
        box.add_widget(button_layout)

        return box

    def show_subscription_popup(self, plan):
        """Show a popup for selected plan."""
        popup_content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        popup_content.add_widget(Label(
            text=f"{self.platform_name} - {plan} Plan",
            halign='center',
            color=(0, 0, 0, 1)
        ))
        close_btn = Button(
            text="Close",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"center_x": 0.5},
            background_color=(0.2, 0.7, 0.2, 1)
        )
        popup_content.add_widget(close_btn)

        popup = Popup(
            title="Subscription Plan",
            content=popup_content,
            size_hint=(0.8, 0.4)
        )
        close_btn.bind(on_release=popup.dismiss)
        popup.open()

    def go_back(self, *args):
        """Return to the Dashboard screen."""
        self.manager.current = 'dashboard'

# Main OTT App
class OTTApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)  # Black Background

        sm = ScreenManager()

        # Add Dashboard Screen
        dashboard_screen = DashboardScreen(name="dashboard")
        sm.add_widget(dashboard_screen)

        # Add Contact Screen
        contact_screen = ContactScreen(name="contact")
        sm.add_widget(contact_screen)

        # Add OTT Platform Screens
        for platform in ["Netflix", "Prime Video", "Disney Hotstar", "zee5"]:
            sm.add_widget(OTTPlatformScreen(platform_name=platform, name=platform.lower().replace(" ", "_")))

        return sm



if __name__ == '__main__':
    OTTApp().run()
