"""
Task:
    - Write a program that creates different types of vehicles (e.g., Car, Truck, Motorcycle) using a factory.
    Each vehicle should have a describe() method that prints a message about the vehicle.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def describe(self):
        """Describe the vehicle."""


class Car(Vehicle):
    def describe(self):
        return "This is a Car. Great for personal use!"


class Truck(Vehicle):
    def describe(self):
        return "This is a Truck. Used for heavy-duty work!"


class Motorcycle(Vehicle):
    def describe(self):
        return "This is a Motorcycle. Perfect for quick rides!"


class VehicleFactory(ABC):
    """Abstract factory class to create vehicles"""

    @abstractmethod
    def create(self):
        """Create a vehicle"""


class CarFactory(VehicleFactory):
    def create(self):
        return Car()


class TruckFactory(VehicleFactory):
    def create(self):
        return Truck()


class MotorcycleFactory(VehicleFactory):
    def create(self):
        return Motorcycle()


def read_vehicle_type(types: list) -> str:
    """Read the vehicle type from user input."""
    while True:
        vehicle_type_input = input("Enter a vehicle type(car, truck, motorcycle): ")
        if vehicle_type_input in types:
            return vehicle_type_input
        print("That's not a valid vehicle type.")


def main(factory: VehicleFactory):
    vehicle = factory.create()
    print(vehicle.describe())


if __name__ == "__main__":
    factories = {
        "car": CarFactory(),
        "truck": TruckFactory(),
        "motorcycle": MotorcycleFactory()
    }
    vehicle_type = read_vehicle_type(list(factories.keys()))
    main(factories[vehicle_type])
