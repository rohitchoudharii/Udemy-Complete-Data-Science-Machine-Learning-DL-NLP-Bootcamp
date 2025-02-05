class Car:
    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def drive(self):
        print(f"I am driving a {self.engine_type} car.")


class Tesla(Car):
    def __init__(self, windows, doors, engine_type, is_self_driving):
        super().__init__(windows, doors, engine_type)
        self.is_self_driving = is_self_driving

    def self_driving(self):
        print(f"Tesla supports self driving: {self.is_self_driving}")


car = Car(4, 5, "Petrol")
car.drive()

tesla = Tesla(4, 5, "Electric", True)
tesla.self_driving()
tesla.drive()


class Animal:
    def __init__(self, species):
        self.species = species


class Pet:
    def __init__(self, name):
        self.name = name

    def show_affection(self):
        print(f"{self.name} shows affection")


class Dog(Animal, Pet):
    def __init__(self, species, name, breed):
        Animal.__init__(self, species)
        Pet.__init__(self, name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks")


dog = Dog("Canine", "Buddy", "Golden Retriever")
dog.make_sound()
dog.show_affection()
dog.bark()
