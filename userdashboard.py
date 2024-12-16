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
from kivy.uix.scrollview import ScrollView

from chatbot import ChatBotScreen
from about import AboutScreen
from faqs import FaqsScreen
from support import SupportScreen



# Dashboard Screen
class UserDashboardScreen(Screen):
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

        buttons = ["Home", "About", "FAQs", "Support", "Contact Us", "Chatbot"]
        for btn_text in buttons:
            button = Button(
                text=btn_text,
                background_color=(0.87, 0.19, 0.39, 1),  # Cherry Red Color
                color=(1, 1, 1, 1),
                font_size='12sp',  # Smaller font size
                size_hint=(None, 1),
                width=100  # Fixed width for buttons
            )
            # Navigation logic for buttons
            if btn_text == "Contact Us":
                button.bind(on_release=self.go_to_contact)
            elif btn_text == "Chatbot":
                button.bind(on_release=self.open_chatbot)
            elif btn_text == "About":
                button.bind(on_release=self.go_to_about)
            elif btn_text == "FAQs":
                button.bind(on_release=self.go_to_faqs)
            elif btn_text == "Support":
                button.bind(on_release=self.go_to_support)

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

    # Methods for navigation
    def go_to_contact(self, instance):
        self.manager.current = "contact"

    def go_to_about(self, instance):
        self.manager.current = "about"

    def go_to_faqs(self, instance):
        self.manager.current = "faqs"

    def go_to_support(self, instance):
        self.manager.current = "support"

    def open_platform_page(self, platform_name):
        self.manager.current = platform_name.lower().replace(" ", "_")

    def open_chatbot(self, instance):
        # Create the chatbot popup window
        chatbot_screen = ChatBotScreen()
        chatbot_popup = Popup(
            title="Chatbot",
            content=chatbot_screen,
            size_hint=(0.8, 0.8)
        )
        chatbot_popup.open()


# Custom OTT Platform Button
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
class OTTPlatformScreen(Screen):
    PLATFORM_PLANS = {
        "Netflix": {"monthly": 649, "yearly": 7788},
        "Prime Video": {"monthly": 460, "yearly": 1900},
        "Disney Hotstar": {"monthly": 460, "yearly": 1900},
        "zee5": {"monthly": 460, "yearly": 1900}
    }

    def __init__(self, platform_name, **kwargs):
        super().__init__(**kwargs)
        self.platform_name = platform_name

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        heading = Label(
            text=f"[b][size=24]{platform_name} Subscription Plans[/size][/b]",
            markup=True,
            font_size='20sp',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.1)
        )
        layout.add_widget(heading)

        plans_container = GridLayout(cols=2, spacing=20, size_hint=(1, 0.8))

        base_plan = self.PLATFORM_PLANS[platform_name]

        self.add_plan_section(
            plans_container,
            title=f"{platform_name} Subscription Plans",
            monthly_price=f"₹{base_plan['monthly']}",
            yearly_price=f"₹{base_plan['yearly']}",
            screens="Four screens at a time"
        )

        self.add_plan_section(
            plans_container,
            title=f"Our {platform_name} Subscription Plans",
            monthly_price=f"₹{base_plan['monthly'] // 4}",
            yearly_price=f"₹{base_plan['yearly'] // 4}",
            screens="One screen at a time",
            add_subscribe=True
        )

        layout.add_widget(plans_container)

        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"center_x": 0.5},
            background_color=(0.8, 0, 0, 1)
        )
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def add_plan_section(self, container, title, monthly_price, yearly_price, screens, add_subscribe=False):
        section = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint=(1, None), height=300)

        heading = Label(
            text=f"[b]{title}[/b]",
            markup=True,
            font_size='18sp',
            color=(1, 0, 0, 1),
            halign="center",
            valign="middle",
            size_hint=(1, 0.2)
        )
        heading.bind(size=heading.setter('text_size'))
        section.add_widget(heading)

        monthly_label = Label(
            text=f"Monthly Price: {monthly_price}\nFeatures:\n- Ultra HD Quality\n- {screens}",
            halign="left",
            valign="top",
            color=(1, 1, 1, 1),
            size_hint=(1, 0.4)
        )
        monthly_label.bind(size=monthly_label.setter('text_size'))
        section.add_widget(monthly_label)

        if add_subscribe:
            monthly_button = Button(
                text="Subscribe",
                size_hint=(None, None),
                size=(120, 40),
                pos_hint={"center_x": 0.5},
                background_color=(0.87, 0.19, 0.39, 1)
            )
            monthly_button.bind(on_release=lambda instance: self.show_popup("Monthly Subscription"))
            section.add_widget(monthly_button)

        yearly_label = Label(
            text=f"Yearly Price: {yearly_price}\nFeatures:\n- Ultra HD Quality\n- {screens}",
            halign="left",
            valign="top",
            color=(1, 1, 1, 1),
            size_hint=(1, 0.4)
        )
        yearly_label.bind(size=yearly_label.setter('text_size'))
        section.add_widget(yearly_label)

        if add_subscribe:
            yearly_button = Button(
                text="Subscribe",
                size_hint=(None, None),
                size=(120, 40),
                pos_hint={"center_x": 0.5},
                background_color=(0.87, 0.19, 0.39, 1)
            )
            yearly_button.bind(on_release=lambda instance: self.show_popup("Yearly Subscription"))
            section.add_widget(yearly_button)

        container.add_widget(section)

    def show_popup(self, subscription_type):
        popup_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        popup_label = Label(
            text=f"You have successfully added the {subscription_type}.",
            halign='center',
            color=(0, 0, 0, 1)
        )
        popup_layout.add_widget(popup_label)

        close_btn = Button(
            text="Close",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"center_x": 0.5},
            background_color=(0.2, 0.7, 0.2, 1)
        )
        popup_layout.add_widget(close_btn)

        popup = Popup(
            title="Subscription Successful",
            content=popup_layout,
            size_hint=(0.8, 0.4)
        )
        close_btn.bind(on_release=popup.dismiss)
        popup.open()

    def go_back(self, *args):
        self.manager.current = 'dashboard'


# Contact Screen (displaying contact info)
class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        contact_label = Label(
            text="[b]Contact Information[/b]\n\nName: Ramya\nPhone: 9177824544",
            markup=True,
            font_size='18sp',
            halign='center',
            color=(1, 1, 1, 1)
        )
        layout.add_widget(contact_label)

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
        self.manager.current = 'dashboard'


# Main OTT App
class OTTApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)  # Black Background

        sm = ScreenManager()

        # Dashboard Screen
        dashboard_screen = UserDashboardScreen(name="dashboard")
        sm.add_widget(dashboard_screen)
        # About Screen
        about_screen = AboutScreen(name="about")
        sm.add_widget(about_screen)
        faqs_screen = FaqsScreen(name="faqs")
        sm.add_widget(faqs_screen)
        support_screen = SupportScreen(name="support")
        sm.add_widget(support_screen)

        # Contact Screen
        contact_screen = ContactScreen(name="contact")
        sm.add_widget(contact_screen)

        # OTT Platform Screens
        for platform in ["Netflix", "Prime Video", "Disney Hotstar", "zee5"]:
            sm.add_widget(OTTPlatformScreen(platform_name=platform, name=platform.lower().replace(" ", "_")))

        return sm


if __name__ == '__main__':
    OTTApp().run()
