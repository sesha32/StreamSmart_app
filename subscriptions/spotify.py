import sqlite3
from datetime import datetime
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from session import SessionManager


from database import initialize_database  # Import the database initialization function

# Initialize the database when the app starts
initialize_database()  # Ensure the database and tables are created before the app runs

Builder.load_file('kv/spotify.kv')

class SpotifyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Placeholder for user data, this should be fetched from your user management system
        self.user_data = {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "mobile": "1234567890"
        }

    def go_back_to_dashboard(self):
        # Navigate to the UserDashboard screen
        self.manager.current = "userdashboard"

    def show_plan_popup(self):
        # Layout for the popup
        layout = FloatLayout()

        # Close button at the top right
        close_button = Button(
            text="X",
            size_hint=(None, None),
            size=(30, 30),
            pos_hint={"right": 0.97, "top": 0.97},
            background_color=(1, 0, 0, 1),  # Red button
            color=(1, 1, 1, 1),  # White text
            bold=True
        )

        # Plan selection buttons
        monthly_button = Button(
            text="Monthly Plan",
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            background_color=(0.2, 0.6, 0.8, 1)
        )
        yearly_button = Button(
            text="Yearly Plan",
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            background_color=(0.2, 0.6, 0.8, 1)
        )

        # Heading for the popup
        heading = Label(
            text="Select a Plan",
            font_size="20sp",
            bold=True,
            size_hint=(None, None),
            pos_hint={"center_x": 0.5, "top": 0.9}
        )

        # Adding widgets to the layout
        layout.add_widget(close_button)
        layout.add_widget(heading)
        layout.add_widget(monthly_button)
        layout.add_widget(yearly_button)

        # Create popup
        popup = Popup(
            title="Select a Plan",
            content=layout,
            size_hint=(0.6, 0.4),
            background="",
            auto_dismiss=False  # Prevent popup from closing when tapping outside
        )

        # Close button functionality
        close_button.bind(on_press=popup.dismiss)

        # Plan button logic to save subscription to database
        monthly_button.bind(on_press=lambda x: self.save_subscription("Monthly Plan", popup))
        yearly_button.bind(on_press=lambda x: self.save_subscription("Yearly Plan", popup))

        # Open the popup
        popup.open()

    def save_subscription(self, plan, popup):
        try:
            # Capture the current timestamp
            applied_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Get user data from the session
            user_data = SessionManager.get_user()  # This will fetch the logged-in user's data

            # Check if the user data is available
            if user_data:
                user_id = user_data["id"]
                first_name = user_data["first_name"]
                last_name = user_data["last_name"]
                email = user_data["email"]
                mobile = user_data["mobile"]

                # Connect to the SQLite database
                conn = sqlite3.connect('streamsmart.db')
                cursor = conn.cursor()

                # Insert subscription data into the netflix_subscriptions table
                cursor.execute('''INSERT INTO spotify_subscriptions (id, first_name, last_name, email, mobile, plan, applied_date)
                                  VALUES (?, ?, ?, ?, ?, ?, ?)''',
                               (user_id, first_name, last_name, email, mobile, plan, applied_date))

                # Commit and close the connection
                conn.commit()

                # Show success message
                self.show_success_message(plan, first_name, mobile)
            else:
                print("No user data found in session!")

        except sqlite3.Error as e:
            print(f"SQLite error while saving subscription: {e}")
        finally:
            conn.close()

        # Close the plan selection popup
        popup.dismiss()


    def show_success_message(self, plan, first_name, mobile):
        # Layout for the success message popup
        layout = FloatLayout()

        # Success message content
        success_message = (
            f"Subscription Successful!\n\n"
            f"Thank you, {first_name}, for subscribing to Spotify on our website.\n\n"
            f"This {plan} requires a team to be formed. We'll notify you once we find a team.\n\n"
            f"We will contact you through your mobile number ({mobile}).\n\n"
            f"Enjoy all the features of the Premium plan!"
        )

        # Label for displaying the message
        message_label = Label(
            text=success_message,
            size_hint=(0.9, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.55},
            halign="center",
            valign="middle",
        )
        message_label.bind(size=message_label.setter('text_size'))  # Wrap text properly

        # OK button
        ok_button = Button(
            text="OK",
            size_hint=(0.3, 0.15),
            pos_hint={"center_x": 0.5, "y": 0.1},
            background_color=(0.2, 0.6, 0.8, 1)
        )

        # Adding widgets to the layout
        layout.add_widget(message_label)
        layout.add_widget(ok_button)

        # Create the success popup
        success_popup = Popup(
            title="Subscription Successful",
            content=layout,
            size_hint=(0.8, 0.6),
            auto_dismiss=False
        )

        # Bind OK button to dismiss the popup
        ok_button.bind(on_press=success_popup.dismiss)

        # Open the success popup
        success_popup.open()
