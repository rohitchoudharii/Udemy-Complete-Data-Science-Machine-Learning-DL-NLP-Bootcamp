tpl = ()
print(type(tpl))

numbers = (1, 2, 3, 4, 5)
print(numbers)

mixed_tuple = (1, "Rohit", 3.14)
print(mixed_tuple)

# Accessing elements of a tuple
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# Slicing a tuple
print(numbers[0:3])
print(numbers[1:4])
print(numbers[2:5])
print(numbers[::])
print(numbers[::2])

# Tuple concatenation
new_tuple = numbers + mixed_tuple
print(new_tuple)

# Tuple repetition
repeated_tuple = numbers * 2
print(repeated_tuple)

# Tuple methods
print(numbers.count(1))
print(numbers.index(3))

# Packin and Unpacking
packed_tuple = 1, 2, 3
print(packed_tuple)
a, b, c = packed_tuple
print(a)
print(b)
print(c)

# unpacking with *
a, *b, c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

# Nested tuples
nested_tuple = ((1, 2), (3, 4, 5), (6, 7))
print(nested_tuple)
print(nested_tuple[2])
print(nested_tuple[2][::2])

# Iterating over a tuple
for i in numbers:
    print(i)
for i in nested_tuple:
    for j in i:
        print(j)
