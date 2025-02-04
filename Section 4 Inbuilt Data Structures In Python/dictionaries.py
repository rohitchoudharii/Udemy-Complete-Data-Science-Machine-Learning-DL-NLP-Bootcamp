empty_dict = {}
print(empty_dict)
print(type(empty_dict))

details = {"name": "Rohit", "age": 20}
print(details)

# Accessing elements
print(details["name"])
print(details["age"])
print(details.get("name"))
print(details.get("age"))
print(details.get("location"))
print(details.get("location", "Location Not found"))

# Adding elements
details["location"] = "Bharat"
print(details)

# Updating elements
details["age"] = 21
print(details)

# Deleting elements
del details["location"]
print(details)

# Dictionary methods
keys = details.keys()
print(keys)
values = details.values()
print(values)

items = details.items()
print(items)

# Shallow copy
details_copy = details.copy()
print(details_copy)

# Iterating over a dictionary by keys
for key in details:
    print(key, details[key])

# Iterating over a dictionary by values
for value in details.values():
    print(value)

# Iterating over a dictionary by items
for key, value in details.items():
    print(key, value)

# nested dictionary
students = {
    "student1": {"name": "Rohit", "age": 20},
    "student2": {"name": "Rohan", "age": 21},
}
print(students["student1"])
print(students["student1"]["name"])
print(students["student1"]["age"])

for student, student_info in students.items():
    print(student)
    print(student_info)
    for key in student_info:
        print(key, student_info[key])

# Dictionary comprehension
# Syntax: {key: value for key, value in iterable}
squares = {i: i * i for i in range(1, 6)}
print(squares)

# Syntax: {key: value for key, value in iterable if condition}
even_squares = {i: i * i for i in range(1, 6) if i % 2 == 0}
print(even_squares)

# Syntax: {key: value for key, value in iterable if condition else value}
even_squares = {i: i * i if i % 2 == 0 else i for i in range(1, 6)}
print(even_squares)

# Dictionary comprehension with nested dictionary
# Syntax: {key: {key: value for key, value in iterable} for key, value in iterable}
nested_squares = {i: {j: j * j for j in range(1, 4)} for i in range(1, 4)}
print(nested_squares)

# Dictionary comprehension with nested dictionary and condition
# Syntax: {key: {key: value for key, value in iterable if condition} for key, value in iterable}
nested_even_squares = {
    i: {j: j * j for j in range(1, 4) if j % 2 == 0} for i in range(1, 4)
}
print(nested_even_squares)

# Merging dictionaries
dict1 = {"name": "Rohit", "age": 20}
dict2 = {"location": "Bharat", "country": "India"}
merged_dict = {**dict1, **dict2}
print(merged_dict)
