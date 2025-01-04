# Violation of OCP
class PaymentProcessor:
    def process_payment(self, payment_type):
        if payment_type == "credit":
            # process credit payment
            pass
        elif payment_type == "paypal":
            # process PayPal payment
            pass

# Following OCP
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self):
        pass

class CreditPayment(PaymentMethod):
    def process(self):
        # process credit payment
        pass

class PaypalPayment(PaymentMethod):
    def process(self):
        # process PayPal payment
        pass

# Usage
def process_payment(payment_method: PaymentMethod):
    payment_method.process()
