from logger import logging


def add(a, b):
    logging.debug(f"The numbers are: {a}, {b}")
    return a + b


add(1, 2)
add(2, 3)
