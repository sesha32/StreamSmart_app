from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import sqlite3
from datetime import datetime, timedelta

class AmazonHavetoissueMonthly(Screen):
    subscriptions_container = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_subscriptions()

    def load_subscriptions(self):
        """Load all monthly subscriptions that are not yet issued."""
        try:
            conn = sqlite3.connect('streamsmart.db')
            cursor = conn.cursor()
            cursor.execute(""" 
                SELECT application_id, id, first_name, email, mobile, applied_date 
                FROM amazon_subscriptions 
                WHERE plan = 'Monthly Plan' AND issued = 'no'""")
            rows = cursor.fetchall()

            self.subscriptions_container.clear_widgets()

            if rows:
                team_subscriptions = []
                for index, row in enumerate(rows, start=1):
                    team_subscriptions.append(row)

                    # Display teams in groups of 4
                    if index % 4 == 0 or index == len(rows):
                        self.add_team_to_ui(team_subscriptions)
                        team_subscriptions = []
            else:
                self.subscriptions_container.add_widget(
                    Label(text="No subscriptions found", color=(1, 1, 1, 1))
                )
        finally:
            conn.close()

    def add_team_to_ui(self, team_subscriptions):
        """Add a team of subscriptions to the UI."""
        team_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=10, padding=10)
        team_layout.height = 200

        # Create GridLayout for table-like structure
        grid_layout = GridLayout(cols=7, size_hint_y=None, spacing=5, padding=5)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        headers = ["Application ID", "ID", "First Name", "Email", "Mobile", "Applied Date", "Delete"]
        for header in headers:
            grid_layout.add_widget(Label(text=header, bold=True, color=(1, 1, 1, 1)))

        # Populate the grid with subscription details
        for subscription in team_subscriptions:
            application_id, id, first_name, email, mobile, applied_date = subscription
            grid_layout.add_widget(Label(text=str(application_id), color=(1, 1, 1, 1)))
            grid_layout.add_widget(Label(text=str(id), color=(1, 1, 1, 1)))
            grid_layout.add_widget(Label(text=first_name, color=(1, 1, 1, 1)))
            grid_layout.add_widget(Label(text=email, color=(1, 1, 1, 1)))
            grid_layout.add_widget(Label(text=mobile, color=(1, 1, 1, 1)))
            grid_layout.add_widget(Label(text=applied_date, color=(1, 1, 1, 1)))

            # Create the delete button
            delete_button = Button(text="Delete", size_hint_y=None, height=30, background_color=(1, 0, 0, 1))
            delete_button.bind(on_release=lambda instance, application_id=application_id: self.delete_subscription(application_id))
            grid_layout.add_widget(delete_button)

        team_layout.add_widget(grid_layout)

        # Add Issue button
        issue_button = Button(text="Issue Team", size_hint_y=None, height=40, background_color=(0, 0.5, 0, 1))
        issue_button.bind(on_release=lambda instance: self.issue_team(team_subscriptions))
        team_layout.add_widget(issue_button)

        self.subscriptions_container.add_widget(team_layout)

    def delete_subscription(self, application_id):
        """Delete a subscription from the database."""
        try:
            conn = sqlite3.connect('streamsmart.db')
            cursor = conn.cursor()

            # Delete the subscription from the database
            cursor.execute("DELETE FROM amazon_subscriptions WHERE application_id = ?", (application_id,))
            conn.commit()

            self.show_popup("Success", f"Subscription {application_id} deleted successfully!")

            # Refresh the subscriptions list
            self.load_subscriptions()
        except sqlite3.Error as e:
            self.show_popup("Error", f"Failed to delete subscription: {str(e)}")
        finally:
            conn.close()

    def issue_team(self, team_subscriptions):
        """Mark the given team as issued and update the database."""
        try:
            conn = sqlite3.connect('streamsmart.db')
            cursor = conn.cursor()
            
            # Fetch the current maximum team_id
            cursor.execute("SELECT MAX(team_id) FROM amazon_subscriptions")
            result = cursor.fetchone()
            team_id = result[0] + 1 if result and result[0] else 1  # Start from 1 if no teams exist

            issued_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Mark each subscription in the team as issued
            for subscription in team_subscriptions:
                application_id, id, _, _, _, _ = subscription
                expire_date = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')

                cursor.execute("""
                    UPDATE amazon_subscriptions 
                    SET issued = 'yes', team_id = ?, issued_date = ?, expire_date = ? 
                    WHERE application_id = ?""", (team_id, issued_date, expire_date, application_id))

                cursor.execute("UPDATE users SET subscriptions = subscriptions + 1 WHERE id = ?", (id,))

            conn.commit()
            self.show_popup("Success", f"Team {team_id} marked as issued successfully!")
            self.load_subscriptions()
        except sqlite3.Error as e:
            self.show_popup("Error", f"Failed to issue team: {str(e)}")
        finally:
            conn.close()

    def show_popup(self, title, message):
        """Show a popup message."""
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

    def go_back(self):
        self.manager.current = "admin_amazon_screen"  # Navigate back to the admin dashboard


# Load the kv file for UI definition
Builder.load_file("kv/amazon_havetoissue_monthly.kv")
