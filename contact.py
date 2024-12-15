from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Overall Layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Contact Title
        title = Label(
            text="[b][size=24]Contact Information[/size][/b]",
            markup=True,
            font_size='20sp',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2)
        )
        layout.add_widget(title)

        # Contact Details
        contact_info = Label(
            text="Name: Ramya\nPhone: 9177824544",
            font_size='18sp',
            halign='center',
            color=(1, 1, 1, 1)
        )
        layout.add_widget(contact_info)

        # Back Button to Return to Dashboard
        back_btn = Button(
            text="Back to Dashboard",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5},
            background_color=(0.87, 0.19, 0.39, 1),  # Cherry red
            color=(1, 1, 1, 1)
        )
        back_btn.bind(on_release=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_back(self, *args):
        self.manager.current = 'dashboard'  # This should correctly switch back to the dashboard screen
