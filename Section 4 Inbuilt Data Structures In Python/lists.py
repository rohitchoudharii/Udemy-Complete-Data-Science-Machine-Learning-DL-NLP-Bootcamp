lst = []
print(type(lst))

names = ["Rohit", "Rahul", "Rajesh", 1, 2, 3, 4, 5]
print(names)

mixed_list = ["Rohit", 20, 1.5, True]
print(mixed_list)

# Accessing elements
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# Negative indexing
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])

# Slicing
print(fruits[0:3])
print(fruits[1:3])
print(fruits[1:])
print(fruits[:3])

# Changing elements
fruits[0] = "Pineapple"
print(fruits)

fruits[1:] = "Watermelon"
print(fruits)


# List methods

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.append("Pineapple")
print(fruits)

fruits.insert(1, "Watermelon")
print(fruits)

fruits.remove("Banana")
print(fruits)

last_el = fruits.pop()
print(last_el)
print(fruits)

index = fruits.index("Mango")
print(index)

fruits.insert(2, "Mango")
print(fruits)
print(fruits.count("Mango"))

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)


# slicing list
# list[start: stop: step]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])

for i in numbers:
    print(i)

for index, value in enumerate(numbers):
    print(index, value)

# List comprehension
# Syntax: [expression for item in iterable]
# Traditional way
squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

# Using list comprehension
squares = [i * i for i in range(1, 11)]
print(squares)

# Syntax: [expression for item in iterable if condition]
# Traditional way
even_squares = []
for i in range(1, 11):
    if i % 2 == 0:
        even_squares.append(i * i)
print(even_squares)

# Using list comprehension
even_squares = [i * i for i in range(1, 11) if i % 2 == 0]

# Syntax: [expression_if if condition else expression_else for item in iterable]
# Traditional way
even_odd_squares = []
for i in range(1, 11):
    if i % 2 == 0:
        even_odd_squares.append("Even")
    else:
        even_odd_squares.append("Odd")
print(even_odd_squares)

# Using list comprehension
even_odd_squares = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 11)]
print(even_odd_squares)

# Syntax: [expression for item in iterable for item in iterable]
# Traditional way
pairs = []
for i in range(1, 3):
    for j in range(1, 3):
        pairs.append((i, j))
print(pairs)

# Using list comprehension
pairs = [(i, j) for i in range(1, 3) for j in range(1, 3)]

# Syntax: [expression for item in iterable for item in iterable if condition]
# Traditional way
even_pairs = []
for i in range(1, 3):
    for j in range(1, 3):
        if (i + j) % 2 == 0:
            even_pairs.append((i, j))
print(even_pairs)

# Using list comprehension
even_pairs = [(i, j) for i in range(1, 3) for j in range(1, 3) if (i + j) % 2 == 0]

# Syntax: [expression_if if condition else expression_else for item in iterable for item in iterable]
# Traditional way
even_odd_pairs = []
for i in range(1, 3):
    for j in range(1, 3):
        if (i + j) % 2 == 0:
            even_odd_pairs.append("Even")
        else:
            even_odd_pairs.append("Odd")
print(even_odd_pairs)

# Using list comprehension
even_odd_pairs = [
    "Even" if (i + j) % 2 == 0 else "Odd" for i in range(1, 3) for j in range(1, 3)
]
print(even_odd_pairs)
