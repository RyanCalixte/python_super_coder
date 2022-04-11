# Data Types :
"""
Strings : "ryan"
Integers : 45
Floats : 3.45
Booleans : True or False
"""

# Data Structures : collection of data types
"""
Lists
Tuples
Dictionaries
Sets
"""

l1 = [1,2,3,4,5]  # Square Bracket
t1 = (1,2,3,4,5)  # Round Bracket

# Lists are mutable and Tuples are immutable.
# mutable -> changeable
# immutable -> unchangeable

print(type(t1))
print(t1[0:3])  # Tuple Slicing


## Tuple with Loops
print("----------------------------")

# i represents index number
i = 0
while i < len(t1):
    print(t1[i])
    i += 1

print("----------------------------")

# i represents index number
for i in range(0, len(t1)):
    print(t1[i])

print("----------------------------")

# i represents the particular element itself
for i in t1:
    print(i)
