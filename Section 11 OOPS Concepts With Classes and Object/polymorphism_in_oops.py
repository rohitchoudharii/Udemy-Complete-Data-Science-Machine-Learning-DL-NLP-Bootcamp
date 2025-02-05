"""
Definitions:
- Method Overriding: Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The overridden method in the subclass should have the same name, parameters, and return type as the method in the superclass.
- Class Interfaces: In Python, class interfaces are defined using abstract base classes (ABCs). An interface specifies a set of methods that a class must implement, but it does not provide the implementation of those methods. Interfaces ensure that a class adheres to a specific contract, making it easier to understand and use the class.

Classes:
- BaseClass: A base class that provides a default implementation of a method.
- SubClass: A subclass that overrides the method from BaseClass to provide a specific implementation.
- InterfaceClass: An abstract base class that defines an interface with abstract methods that must be implemented by any subclass.

Methods:
- BaseClass.method_to_override(self): A method in the base class that can be overridden by subclasses.
- SubClass.method_to_override(self): An overridden method in the subclass that provides a specific implementation.
- InterfaceClass.abstract_method(self): An abstract method that must be implemented by any subclass of InterfaceClass.
"""


class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog()
print(dog.speak())

cat = Cat()
print(cat.speak())


def animal_speak(animal):
    print(animal.speak())


animal_speak(dog)
animal_speak(cat)


class Shape:
    def area(self):
        return "area"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)


def display_area(shape):
    print("Area is ", shape.area())


rectangle = Rectangle(5, 4)
circle = Circle(3)
display_area(rectangle)
display_area(circle)


from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"


class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"


car = Car()
bike = Bike()

print(car.start_engine())
print(bike.start_engine())
