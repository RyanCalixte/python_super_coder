# Methods :

"""
1. count() method
2. sort() method
"""

fruits = ["Apple", "Orange", "Pear", "Mango", "Grapes"]

# count() method -> It counts the no. of times a particular element occurs in a list.
print(fruits.count("Apple"))

# sort() method -> It sorts all the elements of the list in an alphabetical order [ or numerical order ] permanently
# print(f"Original List : {fruits}")
# fruits.sort()
# print(f"Sorted List : {fruits}")

# Function : sorted() function -> It sorts all the elements of the list in an alphabetical order [ or numerical order ] temporarily
print(f"Original List : {fruits}")
print(f"Sorted List : {sorted(fruits)}")
