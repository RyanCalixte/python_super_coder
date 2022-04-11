number = input("Insert the number : ") # 123

FirstDiget = number[0]
# CheckNumber = 1
# DigetCheck = number[CheckNumber]
# DigetAmount = 0
# while DigetCheck != FirstDiget:
#     DigetCheck = number[CheckNumber]
#     CheckNumber = CheckNumber + 1
#     DigetAmount = DigetAmount + 1
#
# Add_Times = 0
# DigetAdd = 0
# Total = 0
# while DigetAdd + 1 < DigetAmount:
#     Total = number[DigetAdd] + number[DigetAdd] + 1
#     DigetAdd = DigetAdd + 1



# print(f"The total is: {Total} with {DigetAmount} digets.")
# Output -> 6

total = 0
for i in number:
    total = total + int(i)

print(total)
