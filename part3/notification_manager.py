import os
import smtplib as mail

from twilio.rest import Client

TWILIO_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = '+14143166728'
TWILIO_VERIFIED_NUMBER = '+351912680064'
EMAIL_FROM = os.environ["MY_EMAIL"]
PASSWORD = os.environ["MY_PASSWORD"]

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
    
    def send_emails(self, email, message):
      connection = mail.SMTP('smtp.gmail.com', 587)
      connection.starttls()
      connection.login(EMAIL_FROM, PASSWORD)
      connection.sendmail(from_addr=EMAIL_FROM,
                         to_addrs=email,
                         msg=f"Subject: Notification from Part 3 \n\n{message}")
      connection.quit()