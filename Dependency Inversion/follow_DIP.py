from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(Notifier):
    def send(self, message):
        print(f"Sending email with message: {message}")


class SmsSender(Notifier):
    def send(self, message):
        print(f"Sending SMS with message: {message}")


class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message):
        self.notifier.send(message)


# Usage
email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.notify("Hello, World!")


sms_sender = SmsSender()
notification_service = NotificationService(sms_sender)
notification_service.notify("Hello, via SMS!")

# Now, the NotificationService class is not tightly coupled to the EmailSender class.
# We can easily add new ways to send notifications without modifying the NotificationService class. This adheres
# to the Dependency Inversion Principle.