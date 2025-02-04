def convert_temperature(temp, unit):
    """This function converts temperature from Celsius to Fahrenheit and vice versa"""
    if unit == "C":
        return temp * 9 / 5 + 32
    elif unit == "F":
        return (temp - 32) * 5 / 9
    else:
        return "Invalid unit"


print(convert_temperature(100, "C"))
print(convert_temperature(212, "F"))
print(convert_temperature(100, "U"))


def is_strong_password(password):
    """This function checks if a password is strong or not"""
    if len(password) < 8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    elif not any(char in "!@#$%^&*()_+" for char in password):
        return False
    else:
        return True


print(is_strong_password("Rohit@123"))
print(is_strong_password("Rohit123"))
print(is_strong_password("rohit@123"))
print(is_strong_password("ROHIT@123"))
print(is_strong_password("Rohit1234"))


def calculate_tota_cost(cart):
    """This function calculates the total cost of items in a cart"""
    total_cost = 0
    for item in cart:
        total_cost += item["price"] * item["quantity"]
    return total_cost


cart = [
    {"name": "apple", "price": 50, "quantity": 2},
    {"name": "banana", "price": 30, "quantity": 3},
    {"name": "orange", "price": 40, "quantity": 4},
]
print(calculate_tota_cost(cart))


def palindrome(string):
    """This function checks if a string is a palindrome or not"""
    return string == string[::-1]


print(palindrome("madam"))


def factorial(n):
    """This function calculates the factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def count_word_frequency(file_path):
    """This function counts the frequency of each word in a sentence"""
    with open(file_path, "r") as file:
        text = file.read()
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower().strip(".,!?;:\"'")
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


print(count_word_frequency("sample_file.txt"))

import re


def is_valid_email(email):
    """This function checks if an email is valid or not"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


print(is_valid_email("test.test.com"))
print(is_valid_email("test@test.com"))
