from abc import ABC, abstractmethod

# Step 1: Create an abstract base class Vehicle
class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass

# Step 2: Modify Car and Motorcycle to inherit from Vehicle
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Motor started")

# Step 3: Create an abstract VehicleFactory class
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Step 4: Implement concrete factory classes
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")

# Step 5: Use factories to create vehicles
def main():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    # Create US Spec vehicles
    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Iron 883")

    us_car.start_engine()
    us_motorcycle.start_engine()

    print("-" * 20)

    # Create EU Spec vehicles
    eu_car = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1250GS")

    eu_car.start_engine()
    eu_motorcycle.start_engine()

if __name__ == "__main__":
    main()
