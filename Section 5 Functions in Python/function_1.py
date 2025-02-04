'''
Syntax:
def function_name(parameters):
    """_summary_
    Args:
        parameters (_type_): _description_

    Returns:
        _type_: _description_
    """
    # function body
    return value
'''


def even_or_odd(num):
    """This function checks if a number is even or odd"""
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


even_or_odd(24)


# Function with multiple parameters
def add(a, b):
    """This function adds two numbers"""
    return a + b


print(add(2, 3))


# Function with default parameters
def greet(name="Guest"):
    """This function greets a person"""
    return "Hello " + name


print(greet("Rohit"))
print(greet())


# Variable length arguments
# positional arguments
def add(*args):
    """This function adds variable number of arguments"""
    sum = 0
    for i in args:
        sum += i
    return sum


# keyword arguments
def details(**kwargs):
    """This function prints the details of a person"""
    for key, value in kwargs.items():
        print(key, value)


# positional and keyword arguments
def add_and_details(*args, **kwargs):
    """This function adds variable number of arguments and prints the details of a person"""
    sum = 0
    for i in args:
        sum += i
    print("Sum:", sum)
    for key, value in kwargs.items():
        print(key, value)


# Function with return statement
def even_or_odd_1(num):
    """This function checks if a number is even or odd"""
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


# Function with multiple return statements
def even_or_odd_2(num):
    """This function checks if a number is even or odd"""
    if num % 2 == 0:
        return "even", num
    return "odd", num
