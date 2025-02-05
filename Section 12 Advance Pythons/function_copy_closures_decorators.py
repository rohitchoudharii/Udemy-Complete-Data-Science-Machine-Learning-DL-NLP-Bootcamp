# Function Copy
def func():
    print("Hello world")


func_copy = func

func_copy()
func_copy()
func_copy()
func_copy()


# function closure
def parent_function():
    def child_function():
        print("Print from child function")

    print("Print from parent function block")
    child_function()


parent_function()


# Decorators
def decorator_func(p_func):
    def child_decorator():
        print("start")
        p_func()
        print("end")

    return child_decorator


@decorator_func
def task_func():
    print("This is a task function")


task_func()


# repeat decorator example
def repeat(n):
    def decorator(func):
        print(func)

        def wrapper(*args, **kwargs):
            print("Wrapper")
            for i in range(n):
                func(*args, **kwargs)

        print("Decorator")
        return wrapper

    print("repeat")
    return decorator


@repeat(5)
def repeat_consumer(n):
    print("Hello new world!", n)


print("Some operatorn")

repeat_consumer("new")
