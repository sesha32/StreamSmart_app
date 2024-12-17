# session.py file (to hold global user session details)
session = {}

class SessionManager:
    _user_data = None  # Class-level variable to store user session data

    @classmethod
    def set_user(cls, user_data):
        """Set user data in the session."""
        cls._user_data = user_data  # Store the session data

    @classmethod
    def get_user(cls):
        """Retrieve full user data from the session."""
        return cls._user_data  # Retrieve the stored session data

    @classmethod
    def clear_session(cls):
        """Clear the session data."""
        cls._user_data = None  # Reset the session data
