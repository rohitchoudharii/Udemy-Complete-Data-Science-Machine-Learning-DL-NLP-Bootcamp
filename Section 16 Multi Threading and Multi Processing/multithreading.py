## Multi Threading

import threading
from time import time, sleep


def print_numbers():
    for i in range(5):
        sleep(2)
        print(f"Number: {i}")


def print_letters():
    for letter in "abcde":
        sleep(2)
        print(f"Letter: {letter}")


t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

start_time = time()
t1.start()
t2.start()

t1.join()
t2.join()

end_time = time()

print(f"Time required: {end_time - start_time}")
