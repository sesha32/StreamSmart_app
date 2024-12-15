from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class FaqsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # About Information
        about_label = Label(
            text=('''Q1: What is StreamSmart?
A: StreamSmart is a platform that enables users to share OTT subscriptions securely and efficiently, making premium streaming services more affordable for individuals and small households.

Q2: How does StreamSmart ensure secure subscription sharing?
A: StreamSmart uses secure account management and encrypted data handling to ensure privacy. Each user in a sharing group has designated access without compromising the original subscription owner's credentials.

Q3: Can I share my subscription with strangers?
A: Yes, StreamSmart allows you to form groups with friends, family, or strangers who match your preferences and availability. It uses an intelligent matching algorithm to ensure compatibility.

Q4: How are costs distributed among group members?
A: Costs are equitably distributed based on the selected plan. StreamSmart provides transparent breakdowns, ensuring each member pays their fair share.

Q5: What happens if a member of the group stops contributing?
A: StreamSmart offers a contingency system. If a member fails to contribute, you can remove them from the group, and the platform will help find a replacement user or adjust the group’s cost distribution.

Q6: Which OTT platforms are supported by StreamSmart?
A: Currently, StreamSmart supports Netflix, Prime Video, Disney+ Hotstar, and Zee5. We are constantly working to expand our platform's compatibility with more streaming services.

Q7: Is it legal to share OTT subscriptions using StreamSmart?
A: StreamSmart operates within the guidelines of OTT platforms by ensuring that shared subscriptions adhere to the original terms of service. Group members are advised to comply with the policies of the respective platforms.

Q8: How can I subscribe to a shared plan?
A: Simply select the OTT platform of your choice, view available sharing groups, and join a group that fits your budget and preferences. Payments are processed securely within the app.

Q9: What payment methods are supported?
A: StreamSmart supports a variety of payment methods, including credit cards, debit cards, UPI, and mobile wallets like Paytm and Google Pay.

Q10: What are the benefits of using StreamSmart?
A: StreamSmart helps reduce subscription costs, optimizes the utilization of multi-device plans, and provides a seamless experience for managing and sharing subscriptions.

'''
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
