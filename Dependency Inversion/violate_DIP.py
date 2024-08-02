class EmailSender:
    def send(self, message):
        print(f"Sending email with message: {message}")

class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()

    def notify_by_email(self, message):
        self.email_sender.send(message)


# Usage
email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.notify("Hey how do you do?")  # Works fine

# The NotificationService class is tightly coupled to the EmailSender class. If we want to add a new way to send notifications, we have to modify the NotificationService class. 
# This violates the Dependency Inversion Principle.

# Now, let's say we want to add a new way to send notifications, for example, via SMS.
# We can add a new class for sending
class SMSSender:
    def send(self, message):
        print(f"Sending SMS with message: {message}")


# And modify the NotificationService class to accept the new sender
class NotificationService:

    def __init__(self):
        self.email_sender = EmailSender()
        self.sms_sender = SMSSender()

    def notify_by_email(self, message):
        self.email_sender.send(message)

    def notify_by_sms(self, message):
        self.sms_sender.send(message)
        
# Usage
notification_service = NotificationService()
notification_service.notify_by_email("Hello, via Email!")
notification_service.notify_by_sms("Hello, via SMS!")