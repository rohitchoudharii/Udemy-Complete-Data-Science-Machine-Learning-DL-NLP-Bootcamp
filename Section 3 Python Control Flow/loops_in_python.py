# For loops
for i in range(0, 5):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 1, -2):
    print(i)

name = "Rohit"
for i in name:
    print(i)

# While loops
counter = 0
while counter < 5:
    print(counter)
    counter += 1


# Loop control statements
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 5 == 0:
        continue
    print(i)

for i in range(10):
    if i == 5:
        pass
    print(i)

# Nested loops
for i in range(3):
    for j in range(3):
        print(i, j)

# test
n = 10
sum = 0
count = 1
while count <= n:
    sum = sum + count
    count += 1
print("Sum of first ", n, " natural numbers is: ", sum)

sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum of first ", n, " natural numbers is: ", sum)

# prime number
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
