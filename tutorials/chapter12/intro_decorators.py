# decorators are used to enhance the functionality of any other function


# We are creating a decorator function
def decorator_function(any_function):
    def wrapper_function():
        print("Hello !")
        any_function()
        print("Hello 2!")
    return wrapper_function


# def func1():
#     print("Hey I am Ryan!")
#
#
# # Standard Way of Creating a Decorator call
# func1_decor = decorator_function(func1)
# func1_decor()


@decorator_function  # syntactic sugar
def func2():
    print("something else")

func2()
