"""
Insert how many numbers you want to have in the list : 2
Insert the number 1 : 4
Insert the number 2 : 3
The List is [4,3]
"""

# Solution :

#i = int(input("Insert how many numbers you want to have in the list: "))
#i2 = 1
#List = []
#while i2 <= i:
    #Numbers = int(input(f"Insert the number {i2} : "))
    #List.append(Numbers)
    #i2 = i2 + 1

#print(f"The list is: {List}")


Amount = int(input("Insert how many numbers you want to have in the list: "))
List = []

for i in range(Amount):
    i = i + 1
    Numbers = int(input(f"Insert the number {i} : "))
    List.append(Numbers)


print(f"The list is: {List}")