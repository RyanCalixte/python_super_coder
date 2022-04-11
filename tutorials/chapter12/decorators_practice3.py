# Define a function which will print numbers from 1 to 10000000.

# Define a decorator which will print out how much time did it take to run the function. Time must be in seconds.

from time import time

def decorator(Func):

    def wrapper():
        Time1 = time()
        Func()
        Time2 = time()
        Total = Time2 - Time1
        print(round(Total,3))
    return wrapper

@decorator
def Printing():
    for i in range(1,100001):
        print(i)

Printing()
# t1 = time()
# for i in range(1,10):
#     print(i)
# t2 = time()
#
# total = t2 - t1
# print(total)
