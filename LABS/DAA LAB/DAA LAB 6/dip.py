# Violation of DIP
class EmailService:
    def send(self, message):
        # logic to send email
        pass

class Notification:
    def __init__(self):
        self.email_service = EmailService()

    def send_notification(self, message):
        self.email_service.send(message)

# Following DIP
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(NotificationService):
    def send(self, message):
        # logic to send email
        pass

class SMSService(NotificationService):
    def send(self, message):
        # logic to send SMS
        pass

class Notification:
    def __init__(self, service: NotificationService):
        self.service = service

    def send_notification(self, message):
        self.service.send(message)

# Usage
email_service = EmailService()
notification = Notification(email_service)
notification.send_notification("Hello World")
