from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget


class ChatBotScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Chat History Display
        self.chat_history = ScrollView(size_hint=(1, 0.8))
        self.chat_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=(10, 10))
        self.chat_box.bind(minimum_height=self.chat_box.setter('height'))
        self.chat_history.add_widget(self.chat_box)
        self.add_widget(self.chat_history)

        # User Input Field
        self.user_input = TextInput(size_hint_y=None, height=50, multiline=False)
        self.add_widget(self.user_input)

        # Send Button
        send_button = Button(text="Send", size_hint_y=None, height=50)
        send_button.bind(on_release=self.send_message)
        self.add_widget(send_button)

    def send_message(self, instance):
        user_message = self.user_input.text.strip()
        if user_message:
            self.display_message(user_message, "User", right_align=True)
            response = self.get_bot_response(user_message)
            self.display_message(response, "Bot", right_align=False)
        self.user_input.text = ""

    def display_message(self, message, sender, right_align):
        # Message Container (for alignment)
        message_container = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=40,
            padding=(5, 0),
            spacing=5,
        )

        if right_align:
            # User message: push message to the right
            spacer = Widget(size_hint_x=0.5)  # Spacer on the left
            message_label = Label(
                text=f"[b]{sender}:[/b] {message}",
                markup=True,
                size_hint_y=None,
                height=40,
                halign="right",
                valign="middle",
                text_size=(self.width * 0.45, None),  # Limit text width to 45% of screen width
                color=(1, 1, 1, 1),  # Black text
            )
            message_label.bind(size=self._update_height)
            message_container.add_widget(spacer)
            message_container.add_widget(message_label)
        else:
            # Bot message: push message to the left
            spacer = Widget(size_hint_x=0.5)  # Spacer on the right
            message_label = Label(
                text=f"[b]{sender}:[/b] {message}",
                markup=True,
                size_hint_y=None,
                height=40,
                halign="left",
                valign="middle",
                text_size=(self.width * 0.45, None),  # Limit text width to 45% of screen width
                color=(1, 1, 1, 1),  # Black text
            )
            message_label.bind(size=self._update_height)
            message_container.add_widget(message_label)
            message_container.add_widget(spacer)

        # Add the message to the chat box
        self.chat_box.add_widget(message_container)
        self.chat_box.height += message_container.height

    def _update_height(self, instance, *args):
        # Adjust height to fit text content
        instance.text_size = (instance.width, None)
        instance.height = instance.texture_size[1]

    def get_bot_response(self, user_message):
        # Simple responses based on user input
        user_message = user_message.lower()
        if 'help' in user_message:
            return "How can I assist you with subscription sharing?"
        elif 'share subscription' in user_message:
            return "You can share your subscription with family or friends. I can guide you!"
        elif 'plan' in user_message:
            return "You can select between Monthly or Yearly plans for each platform."
        elif 'cost' in user_message:
            return "The cost is equally divided among the users sharing the subscription."
        else:
            return "Sorry, I didn't quite get that. Could you please rephrase?"
