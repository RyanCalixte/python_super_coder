from functools import wraps

def decorator(any_func):
    @wraps(any_func)
    def wrapper():
        """Here's me! The Wrapper Function."""
        print(f"You are executing {any_func.__name__}")
        print(f"Help for the function: {any_func.__doc__}")
        any_func()
    return wrapper


@decorator
def func1_something():
    """this is func1_something which is doing something."""
    print("Here is the function 1")

func1_something()

print("---------------------------")


print(func1_something.__name__)
print(func1_something.__doc__)