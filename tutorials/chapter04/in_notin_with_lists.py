names = ["alan", "joe", "john", "mark"]
i = 0

user_input = input("Insert the name: ")
# NameValid = False
# for i in range(4):
#     if user_input == names[i]:
#         NameValid = True
#         print("Your name exist.")
#     elif names[i] == names[-1] and NameValid == False:
#         print("Your name does not exist")
#     i = i + 1

if user_input in names:
    print("It exists")
else:
    print("Doesn't exists")
