# Lists

# NumAmount = int(input("How many numbers do you want to insert?"))

# OutputList = []
# Addition = 0
# for i in range(0,NumAmount):
#      Num = int(input("Insert a number: "))
#      OutputList.append(Num)
#      Addition = Addition + Num
# i = 0
# while i < NumAmount:
#     Num = int(input("Enter a number: "))
#     OutputList.append(Num)
#     Addition = Addition + Num
#     i = i + 1
# OutputList.append(Addition)
# print(f"Here's your list: {OutputList}")

# from operator import truediv
# from telnetlib import theNULL
# from typing import List


# String1 = input("Insert the first string: ")
# String2 = input("Insert the second string: ")
# String3 = input("Insert the third string: ")
# String4 = input("Insert the fourth string: ")


# def Listing(*args):
#     List = []
#     Output = []
#     for i in args:
#         List.append(i)
#     print(f"These are the original values: {String1} {String2} {String3} {String4}")
#     CommonLetter = ""
#     NonCommonStrings = String1+" "+String2
   
#     string = ""
#     for j in List:
        
#         for k in j:
#             for h in string:
#                 if k == h:
#                     CommonLetter = CommonLetter + k
#         string = j
    
#     Output.append(NonCommonStrings)
#     Output.append(CommonLetter)
#     print(f"Converted Values: {Output}")

        
        
    


# Listing(String3,String4)

from doctest import OutputChecker


Integir = int(input("Insert a number: "))
Ouput = {}
for i in range(1,Integir + 1):
    
    Ouput[i] = i*i*i
print(Ouput)