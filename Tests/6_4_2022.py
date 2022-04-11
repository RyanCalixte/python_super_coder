# 123 - 196

# while loop
# i = 123
# while i < 197:
#     print(i)
#     i = i + 1


# for loop
# for j in range(123,197):
#     print(j)

# Sum up numbers from 1 to 10 = 55
# Sum = 0
# for i in range(1,11):
#     Sum = Sum + i
# print(Sum)

#  Sum up numbers from 10 to 20
# Sum = 0
# i = 10
# while i < 21:
#     Sum = Sum + i
#     i = i + 1
# print(Sum)

# Create a function called as 'greatest' which returns the greatest number out of 4 numbers.
GreatestNum = 0


def greatest(*args):
    print(max(args))

greatest(1, 6, 17, 17)


# Create a function which prints out the mathematical table of the specified number
# 3x4 = 12

Number = int(input("Insert a number: "))

def Table(Num):
    for i in range(1,11):
        print(f"{Number} x {i} = {Number*i}")


Table(Number)