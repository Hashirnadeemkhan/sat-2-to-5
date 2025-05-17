from abc import ABC, abstractmethod

# 1. Define the Abstract Base Class (ABC)
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Processes a payment and returns True on success, False otherwise."""
        pass

    @abstractmethod
    def refund_payment(self, transaction_id: str) -> bool:
        """Refunds a payment and returns True on success, False otherwise."""
        pass

    def get_processor_name(self) -> str:
        """A concrete method available to all processors."""
        return self.__class__.__name__

# 2. Implement Concrete Payment Processors
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount:.2f}...")
        # Simulate complex credit card API interaction
        # In a real app, this would involve network calls, error handling etc.
        return True

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Refunding credit card transaction {transaction_id}...")
        # Simulate credit card refund API interaction
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount:.2f}...")
        # Simulate complex PayPal API interaction
        return True

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Refunding PayPal transaction {transaction_id}...")
        # Simulate PayPal refund API interaction
        return True

# 3. Using the Abstraction
def handle_transaction(processor: PaymentProcessor, amount: float, transaction_id: str = None):
    print(f"\n--- Handling transaction with {processor.get_processor_name()} ---")
    if processor.process_payment(amount):
        print("Payment successful!")
        # Later, if needed:
        # processor.refund_payment(transaction_id)
    else:
        print("Payment failed!")

# Client code can interact with any payment processor interchangeably
credit_card_proc = CreditCardProcessor()
paypal_proc = PayPalProcessor()

handle_transaction(credit_card_proc, 150.00)
handle_transaction(paypal_proc, 75.50, "PYPL_REFUND_123") # Example of refund param