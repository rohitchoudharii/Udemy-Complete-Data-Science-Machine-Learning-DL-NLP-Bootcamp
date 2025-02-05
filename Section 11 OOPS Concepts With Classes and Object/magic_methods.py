class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


# Example usage
person = Person("Alice", 30)
print(person)  # Output: Person(name=Alice, age=30)
