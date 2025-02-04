numbers = [1, 2, 3, 4, 5]


def squares_func(n):
    return n**2


print(list(map(squares_func, numbers)))
print(list(map(lambda n: n**2, numbers)))

# Map multiple iterables
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [5, 4, 3, 2, 1]

print(list(map(lambda n1, n2: n1 + n2, numbers1, numbers2)))

# Map to convert string to int
numbers = ["1", "2", "3", "4", "5"]
print(list(map(int, numbers)))

# Map to upper case all elements in a list
names = ["john", "doe", "jane"]
print(list(map(str.upper, names)))

# extract name from a list of dictionaries
people = [{"name": "john", "age": 25}, {"name": "doe", "age": 30}]
print(list(map(lambda person: person["name"], people)))
