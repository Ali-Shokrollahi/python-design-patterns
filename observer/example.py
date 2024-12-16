"""
Task:
    - building a system to monitor the price of a product and notify subscribed users when the price changes.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, changed_product: 'Subject', old_price: float):
        ...


class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        ...

    @abstractmethod
    def remove_observer(self, observer: Observer):
        ...

    @abstractmethod
    def notify_observers(self, old_price: float):
        ...


class Product(Subject):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self._observers = []

    def set_price(self, new_price: float):
        if self.price != new_price:
            old_price = self.price
            self.price = new_price
            self.notify_observers(old_price)


    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, old_price: float):
        for observer in self._observers:
            observer.update(self, old_price)


class User(Observer):
    min_price_notification = 5

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def set_min_price_change_notify(self, min_price: float):
        self.min_price_notification = min_price

    def update(self, changed_product: Product, old_price: float):
        price_difference = abs(changed_product.price - old_price)
        if price_difference >= self.min_price_notification:
            print(f"Sending email to {self.email}: {changed_product.name} new price is {changed_product.price}")


if __name__ == "__main__":
    product = Product("Laptop", 1000)
    alice = User("Alice", email="alice@email.com")
    alice.set_min_price_change_notify(50)
    bob = User("Bob", email="bob@email.com")
    bob.set_min_price_change_notify(20)

    product.add_observer(alice)
    product.add_observer(bob)

    product.set_price(980.0)  # Notify Alice only (change = $20, below Bob's threshold)
    product.set_price(920.0)  # Notify both (change = $60, above both thresholds)
    product.set_price(910.0)  # Notify Bob only (change = $10, below Alice's threshold)
