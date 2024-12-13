from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/admin_dashboard.kv')


class AdminDashboardScreen(Screen):
    def logout(self):
        # Clear the email and password fields before navigating to login
        login_screen = self.manager.get_screen('login')
        login_screen.ids.username.text = ''
        login_screen.ids.password.text = ''
        
        # Navigate to the login screen
        self.manager.current = 'login'
