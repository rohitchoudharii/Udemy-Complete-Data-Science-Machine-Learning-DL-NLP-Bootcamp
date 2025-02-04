numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def even_func(n):
    return n % 2 == 0


print(list(filter(even_func, numbers)))
print(list(filter(lambda n: n % 2 == 0, numbers)))

# Filter with multiple conditions
print(list(filter(lambda n: n % 2 == 0 and n > 9, numbers)))

# Filter students who passed
students = [
    {"name": "john", "score": 30},
    {"name": "doe", "score": 50},
    {"name": "jane", "score": 40},
    {"name": "jane", "score": 70},
]
print(list(filter(lambda student: student["score"] > 40, students)))
