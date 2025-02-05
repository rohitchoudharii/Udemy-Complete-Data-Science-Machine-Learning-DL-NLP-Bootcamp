class Car:
    pass


tata = Car()
audi = Car()

tata.window = 4
audi.doors = 4

print(tata)
print(audi)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof")


dog1 = Dog("Bruno", 5)
dog2 = Dog("Lunar", 3)
print(dog1)
print(dog2)

dog1.bark()
dog2.bark()


# Modeling a bank account
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        pass

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print("Your final balance is ", self.balance)

    def get_balance(self):
        return self.balance


account = BankAccount("John", 10000)
account.deposit(100)
account.withdraw(300)
print("Balance is", account.get_balance())
account.withdraw(11000)
