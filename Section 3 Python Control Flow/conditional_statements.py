age = 20

if age >= 18:
    print("You are an adult")

if age < 18:
    print("You are a minor")

# Using else
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Using elif
age = 5
if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
else:
    print("You are an adult")

# nested conditional statements
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")

# Simple Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid operation")
