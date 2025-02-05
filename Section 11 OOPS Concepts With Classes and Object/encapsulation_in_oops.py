class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age  # Protected attribute

    # Getter for name
    def get_name(self):
        return self.name

    # Setter for name
    def set_name(self, name):
        self.name = name

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, age):
        self._age = age


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary  # Private attribute

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        self.__salary = salary


# Creating an object of Employee
emp = Employee("John", 30, 50000)

# Accessing public attribute
print("Name:", emp.name)

# Accessing protected attribute
print("Age:", emp._age)

# Accessing private attribute using getter
print("Salary:", emp.get_salary())

# Modifying attributes using setters
emp.set_name("Doe")
emp.set_age(35)
emp.set_salary(60000)

# Accessing modified attributes
print("Modified Name:", emp.get_name())
print("Modified Age:", emp.get_age())
print("Modified Salary:", emp.get_salary())
