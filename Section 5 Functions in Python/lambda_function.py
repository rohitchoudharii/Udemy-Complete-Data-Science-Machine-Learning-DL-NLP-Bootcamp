"""
#Syntax
lambda arguments: expression
"""


def add(a, b):
    return a + b


add_lambda = lambda a, b: a + b

print(type(add_lambda))
print(add(2, 3))
print(add_lambda(2, 3))

even_ = lambda x: x % 2 == 0
print(even_(2))

multiple_add = lambda a, b, c: a + b + c
print(multiple_add(2, 3, 4))
