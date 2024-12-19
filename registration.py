from email.mime.text import MIMEText
import smtplib
import sqlite3
import bcrypt
import random
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/registration.kv')

class RegistrationScreen(Screen):
    def register_user(self):
        first_name = self.ids.first_name.text
        last_name = self.ids.last_name.text
        email = self.ids.email.text
        mobile = self.ids.mobile.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_password.text

        if password != confirm_password:
            print("Passwords do not match!")
            return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Generate OTP
        otp = random.randint(100000, 999999)

        try:
            conn = sqlite3.connect("streamsmart.db")
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO users (first_name, last_name, email, mobile, password, subscriptions, otp)
                               VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (first_name, last_name, email, mobile, hashed_password, 0, otp))
            conn.commit()
            conn.close()

            # Send OTP via email
            self.send_otp_email(email, otp)

            print("User registered successfully and OTP sent!")
            self.manager.current = 'login'
        except sqlite3.IntegrityError:
            print("This email is already registered!")

    def send_otp_email(self, email, otp):
        # Assuming you're using a Gmail SMTP server
        sender_email = "youremail@gmail.com"
        sender_password = "yourpassword"
        
        # Create the email content
        subject = "Your OTP Code"
        body = f"Your OTP code for registration is {otp}."
        
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = email

        try:
            # Connect to the server
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())
            print("OTP sent to email!")
        except Exception as e:
            print(f"Error sending email: {e}")
