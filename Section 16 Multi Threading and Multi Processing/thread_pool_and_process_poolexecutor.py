from concurrent.futures import ThreadPoolExecutor
import time


def print_number(number):
    time.sleep(1)
    return f"Number: {number}"


numbers = [
    1,
    2,
    3,
    4,
    5,
    4,
    5,
    3,
    4,
    5,
    6,
    7,
    7,
    8,
    54,
    32,
    345,
    67,
    654,
    32,
    34,
    5,
    43,
]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

for result in results:
    print(result)

from concurrent.futures import ProcessPoolExecutor


def square_numbers(number):
    time.sleep(1)
    return f"Square: {number**2}"


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor2:
        results = executor2.map(square_numbers, numbers)
    for result in results:
        print(result)
