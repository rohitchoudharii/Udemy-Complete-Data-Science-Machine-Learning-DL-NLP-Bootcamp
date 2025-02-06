import logging

## logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler("app1.log"), logging.StreamHandler()],
)

logger = logging.getLogger("ArithmethicApp")


def add(a, b):
    logger.debug(f"Adding a: {a} b:{b} = {a + b}")


def sub(a, b):
    logger.debug(f"Substracting a: {a} b:{b} = {a - b}")


def mul(a, b):
    logger.debug(f"Multiplying a: {a} b:{b} = {a * b}")


def div(a, b):
    try:
        logger.debug(f"Diviting a: {a} b:{b} = {a / b}")
    except ZeroDivisionError:
        logger.error("Denominator can't be zero")


num1 = int(input("Input Number 1"))
num2 = int(input("Input Number 2"))

add(num1, num2)
sub(num1, num2)
mul(num1, num2)
div(num1, num2)
