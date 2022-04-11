
def Dec(Func):

    def wrapper(*args, **kwargs):
        print(Func.__doc__)

        return Func(*args, **kwargs)
    return wrapper

@Dec
def Adding(a,b):
    """This function is adding two numbers."""
    return a+b

print(Adding(2,3))
