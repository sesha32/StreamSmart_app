import sqlite3
import bcrypt
import random
import smtplib
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from email.mime.text import MIMEText

Builder.load_file('kv/forgot_password.kv')

class ForgotPasswordScreen(Screen):
    otp = None  # Store the OTP for verification
    email = None  # Store the email entered by the user

    def send_otp_email(self, email):
        """Generate a random OTP and send it to the user's email."""
        otp = str(random.randint(100000, 999999))
        
        # Send OTP to the user's email
        try:
            msg = MIMEText(f"Your OTP is {otp}")
            msg['Subject'] = 'Password Reset OTP'
            msg['From'] = 'your_email@example.com'  # Replace with your email
            msg['To'] = email

            # Setup the SMTP server
            with smtplib.SMTP('smtp.example.com', 587) as server:  # Use your SMTP server
                server.starttls()
                server.login('your_email@example.com', 'your_password')  # Use your email credentials
                server.sendmail('your_email@example.com', email, msg.as_string())
                
            print("OTP sent to email!")
            return otp  # Return OTP to verify later
        except Exception as e:
            print(f"Error sending OTP email: {e}")
            return None

    def verify_email(self):
        """Verify the entered email and send the OTP to it."""
        email = self.ids.email.text.strip()

        # Check if email is provided
        if not email:
            print("Please enter an email address.")
            return

        # Send OTP to the email
        self.otp = self.send_otp_email(email)  # Send OTP and store it

        # Store the email address entered by the user
        self.email = email

        if self.otp:
            # Enable OTP input field after sending OTP
            self.ids.otp.disabled = False
            self.ids.otp.focus = True  # Focus on OTP input field
            print("OTP has been sent to your email.")
        else:
            print("Failed to send OTP. Try again.")

    def reset_password(self):
        """Reset the password if OTP and passwords are correct."""
        new_password = self.ids.new_password.text.strip()
        confirm_password = self.ids.confirm_password.text.strip()
        entered_otp = self.ids.otp.text.strip()  # OTP entered by the user

        # Check if all fields are filled
        if not new_password or not confirm_password or not entered_otp:
            print("Please fill all fields!")
            return

        # Verify OTP
        if entered_otp != self.otp:
            print("Invalid OTP!")
            return

        # Check if new passwords match
        if new_password != confirm_password:
            print("Passwords do not match!")
            return

        try:
            # Connect to the database
            conn = sqlite3.connect("streamsmart.db")
            cursor = conn.cursor()

            # Fetch user data by email
            cursor.execute("SELECT id, first_name, last_name, email, mobile, password FROM users WHERE email=?", (self.email,))
            user_data = cursor.fetchone()

            if user_data:
                user_id, first_name, last_name, email, mobile, stored_password = user_data

                # Hash the new password before saving it
                hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

                # Update the password in the database
                cursor.execute("UPDATE users SET password=? WHERE email=?", (hashed_new_password, self.email))
                conn.commit()

                print("Password updated successfully!")
                self.manager.current = 'login'  # Redirect to login screen after success
            else:
                print("User not found!")

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def on_email_enter(self):
        """Move focus to the OTP input field when Enter is pressed in the email field."""
        email = self.ids.email.text.strip()
        if not email:
            print("Please enter an email address.")
            return
        
        self.verify_email()
        self.ids.otp.focus = True  # Focus to OTP field after pressing Enter

    def on_otp_enter(self):
        """Move focus to the new password input field when Enter is pressed in the OTP field."""
        entered_otp = self.ids.otp.text.strip()
        if not entered_otp:
            print("Please enter OTP.")
            return
        
        self.ids.new_password.focus = True  # Focus to new password field

    def on_new_password_enter(self):
        """Move focus to the confirm password input field when Enter is pressed in the new password field."""
        self.ids.confirm_password.focus = True

    def on_confirm_password_enter(self):
        """Trigger password reset when Enter is pressed in the confirm password field."""
        self.reset_password()
