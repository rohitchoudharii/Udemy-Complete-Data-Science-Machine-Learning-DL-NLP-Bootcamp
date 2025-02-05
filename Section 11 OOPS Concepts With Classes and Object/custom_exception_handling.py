class CustomException(Exception):
    pass


class AgeRangeException(CustomException):
    pass


age = int(input("Enter your age"))
try:
    if age > 20 and age < 30:
        print("You are in the age bracket")
    else:
        raise AgeRangeException()
except CustomException:
    print("Yo do not fall in the age bracket")
