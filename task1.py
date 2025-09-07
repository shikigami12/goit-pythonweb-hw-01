from abc import ABC, abstractmethod
from typing import Type

from logger import logger


# Step 1: Create an abstract base class Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Step 2: Modify Car and Motorcycle to inherit from Vehicle
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Engine started")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Motor started")


# Step 3: Create an abstract VehicleFactory class
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


# Step 4: Implement concrete factory classes
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# Step 5: Use factories to create vehicles
def main() -> None:
    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    # Create US Spec vehicles
    us_car: Car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle: Motorcycle = us_factory.create_motorcycle(
        "Harley-Davidson", "Iron 883"
    )

    us_car.start_engine()
    us_motorcycle.start_engine()

    logger.info("-" * 20)

    # Create EU Spec vehicles
    eu_car: Car = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle: Motorcycle = eu_factory.create_motorcycle("BMW", "R1250GS")

    eu_car.start_engine()
    eu_motorcycle.start_engine()


if __name__ == "__main__":
    main()
