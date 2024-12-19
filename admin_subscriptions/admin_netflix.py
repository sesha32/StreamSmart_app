from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty
from kivy.lang import Builder

Builder.load_file('kv/admin_netflix.kv')

class AdminNetflixScreen(Screen):
    def navigate_to_plan(self, plan_type):
        if plan_type == "Monthly Plan":
            self.manager.current = "netflix_havetoissue_monthly"  # Navigate to the NetflixHaveToIssueMonthly page
        elif plan_type == "Yearly Plan":
            self.manager.current = "netflix_havetoissue_yearly"  # Navigate to the NetflixHaveToIssueYearly page
        else:
            print(f"Unknown plan type: {plan_type}")  # Handle other plan types if needed

    def go_back(self):
        self.manager.current = "admindashboard"  # Navigate back to the admin dashboard
