from abc import ABC, abstractmethod


class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("The engine is started")


car = Car()

car.start_engine()
car.drive()
