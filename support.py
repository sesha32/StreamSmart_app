from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class SupportScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # About Information
        about_label = Label(
            text=(
                "Email:abc@gmail.com"
                "Contact:1234567890"
                "website:abc.com"
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
        self.manager.current = 'dashboard'
