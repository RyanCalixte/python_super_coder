# def Transfer(L):
#     Output = []
#     for i in range(0,5):
#         if len(L[i]) == 4:
#             Output.append(L[i].upper())
#
#         elif len(L[i]) == 5:
#             for j in L:
#                 m = list[j]
#                 FirstLetter = m[0]
#                 FirstLetter_String = str(m[0])
#                 FirstLetter_String = FirstLetter_String.upper()
#             Output.append(FirstLetter_String)
#
#
#     print(Output)


# Return the first letter of each argument as a capital with the rest being lowercase.
# ["rYan", "KAUstubh"] -> ["Ryan", "Kaustubh"]

def transfer(l):
    new_list = []
    for i in l:
        if len(i) == 5:
            upper = i[0].upper()
            lower = i[1:].lower()
            new = upper + lower
            new_list.append(new)
        else:
            new_list.append(i.upper())

    return new_list



# First letter uppercase
# Rest of the letters lowercase


print(transfer(["alan","steve","macel","rance","john"]))