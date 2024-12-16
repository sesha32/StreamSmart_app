from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window


class ChatBotScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Adjust window size
        Window.size = (600, 700)

        self.username = "User"  # Placeholder for username
        self.current_category = None  # Track the current question category
        self.feedback_collected = False

        # Chat History Display
        self.chat_history = ScrollView(size_hint=(1, 0.85))
        self.chat_box = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=10,
            padding=(10, 10)
        )
        self.chat_box.bind(minimum_height=self.chat_box.setter('height'))
        self.chat_history.add_widget(self.chat_box)
        self.add_widget(self.chat_history)

        # Input Field and Send Button
        input_layout = BoxLayout(size_hint_y=None, height=60)
        self.user_input = TextInput(
            hint_text="Type your feedback here...",
            multiline=False,
            size_hint_x=0.8,
            disabled=True  # Input is disabled until feedback is needed
        )
        send_button = Button(text="Send", size_hint_x=0.2)
        send_button.bind(on_release=self.process_feedback)
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_button)
        self.add_widget(input_layout)

        # Send initial greeting message
        self.bot_message(f"Hi {self.username}! Welcome to our chatbot. How can I assist you today?")
        self.present_main_menu()

    def bot_message(self, message):
        self.display_message(message, "Bot", right_align=False)

    def user_message(self, message):
        self.display_message(message, "User", right_align=True)

    def display_message(self, message, sender, right_align):
        """Displays text-based messages with proper alignment."""
        message_container = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            spacing=10,
        )

        message_label = Label(
            text=f"[b]{sender}:[/b] {message}",
            markup=True,
            size_hint_y=None,
            halign="right" if right_align else "left",
            valign="middle",
            text_size=(self.width * 0.7, None),
        )
        message_label.bind(size=self._update_height)

        spacer = Widget(size_hint_x=0.2)
        if right_align:
            message_container.add_widget(spacer)
            message_container.add_widget(message_label)
        else:
            message_container.add_widget(message_label)
            message_container.add_widget(spacer)

        self.chat_box.add_widget(message_container)

    def display_link(self, text, callback):
        """Displays clickable links (Buttons) as chat options aligned to the left."""
        button = Button(
            text=text,
            size_hint_y=None,
            height=40,
            background_color=(0, 0, 0, 0),
            color=(0, 0.5, 1, 1),  # Blue link color
            underline=True,
            halign="left",
            size_hint_x=1  # Ensure the button takes up the full width
        )
        button.bind(on_release=callback)
        self.chat_box.add_widget(button)

    def _update_height(self, instance, *args):
        instance.text_size = (instance.width, None)
        instance.height = instance.texture_size[1] + 10

    def process_feedback(self, instance):
        """Collect user feedback."""
        feedback = self.user_input.text.strip()
        if feedback:
            self.user_message(feedback)
            self.bot_message("Thank you for your valuable feedback! Have a great day!")
            self.user_input.text = ""
            self.user_input.disabled = True  # Disable feedback input
            self.feedback_collected = True

    def present_main_menu(self):
        self.bot_message("What would you like to know about our application?")
        self.display_link("1. Related to Subscription Plan", lambda x: self.present_sub_questions("subscription plan"))
        self.display_link("2. Related to OTT Platforms", lambda x: self.present_sub_questions("ott platforms"))
        self.display_link("3. Related to Security", lambda x: self.present_sub_questions("security"))
        self.display_link("4. Related to Legality Issues", lambda x: self.present_sub_questions("legality issues"))

    def present_sub_questions(self, category):
        self.current_category = category
        self.user_message(f"Selected: {category.capitalize()}")
        if category == "subscription plan":
            self.display_link("1. What plans do you offer?", lambda x: self.show_answer("What plans do you offer?", "We offer Basic, Standard, and Premium plans."))
            self.display_link("2. How much does it cost?", lambda x: self.show_answer("How much does it cost?", "Our plans range from $5 to $20 per month."))
        elif category == "ott platforms":
            self.display_link("1. What platforms are supported?", lambda x: self.show_answer("What platforms are supported?", "We support Netflix, Amazon Prime, Disney+, and more."))
            self.display_link("2. How to link my account?", lambda x: self.show_answer("How to link my account?", "Go to Settings > Link Account > Follow the instructions."))
        elif category == "security":
            self.display_link("1. How secure is my data?", lambda x: self.show_answer("How secure is my data?", "We use 256-bit encryption to secure all data."))
            self.display_link("2. What measures are in place to protect me?", lambda x: self.show_answer("What measures are in place to protect me?", "We implement multi-factor authentication and secure payments."))
        elif category == "legality issues":
            self.display_link("1. Is subscription sharing legal?", lambda x: self.show_answer("Is subscription sharing legal?", "Subscription sharing depends on the platform's terms of service."))
            self.display_link("2. Are there any risks involved?", lambda x: self.show_answer("Are there any risks involved?", "Sharing accounts may lead to account suspension."))

    def show_answer(self, question, answer):
        """Display the answer to a clicked question and ask for satisfaction."""
        self.user_message(question)  # Show the clicked question text
        self.bot_message(answer)
        self.ask_satisfaction()

    def ask_satisfaction(self):
        """Ask if the user is satisfied with the answer."""
        self.bot_message("Are you satisfied with my answer?")
        self.display_link("Yes", lambda x: self.collect_feedback())
        self.display_link("No", lambda x: self.represent_questions())

    def represent_questions(self):
        """Re-present the questions for the current category."""
        self.bot_message("Let me present the questions again for you.")
        self.present_sub_questions(self.current_category)

    def collect_feedback(self):
        """Ask the user for feedback."""
        self.bot_message("I'm glad I could help! Please provide your feedback below.")
        self.user_input.disabled = False  # Enable feedback input


class ChatBotApp(App):
    def build(self):
        return ChatBotScreen()


if __name__ == "__main__":
    ChatBotApp().run()
