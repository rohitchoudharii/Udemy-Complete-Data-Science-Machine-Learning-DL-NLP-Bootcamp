"""try:
    # Code that may raise an exception
    pass
except SomeException as ex:
    # Code that runs if the exception occurs
    pass
else:
    # Code that runs if no exception occurs
    pass
finally:
    # Code that runs no matter what
    pass
"""

try:
    a = b
except:
    print("Some name is not defined")

try:
    a = b
except NameError as ex:
    print(ex)

try:
    result = 1 / 0
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter a valid dinominator")

try:
    result = 1 / 2
    a = b
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter a valid dinominator")
except Exception as ex:
    print(ex)
    print("Main exception got caught")

try:
    result = 1 / (int(input("Enter value")))
except Exception as ex:
    print(ex)
else:
    print("THe result is: ", result)
finally:
    print("Execution complete")

try:
    file = open(
        "/Users/rohit/Coding/Learning/Complete Data Science,Machine Learning,DL,NLP Bootcamp/Section 9 File Handling in Python/files/example_copy.txt",
        "r",
    )
    a = b
except FileNotFoundError as ex:
    print(ex)
except Exception as ex:
    print("Some other error: ", ex)
finally:
    print("file variable", "file" in locals())
    print("file is closed", file.closed)
    if "file" in locals() and not file.closed:
        file.close()
        print("Closing file")
