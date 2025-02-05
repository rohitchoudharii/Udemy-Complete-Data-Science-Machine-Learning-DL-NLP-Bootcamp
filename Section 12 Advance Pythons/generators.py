def generate_numbers(n):
    for i in range(n):
        yield i


for i in generate_numbers(5):
    print(i)


print("Multiple yeild")


def multiple_yield(n):
    for i in range(n):
        yield i
    for i in range(0, n, 2):
        yield i
    for i in range(0, n, 5):
        yield i


def multiple_yield_eg_2():
    yield 1
    yield 2
    yield 3


for j in multiple_yield(10):
    print(j)

for i in multiple_yield_eg_2():
    print(i)
