# Unordered collection of unique elements.
# Sets are defined using curly brackets

s = {4,5,6,3,3}
print(s)


l = [1,2,3,3,4,4,4,5,6,5,7,8,5,5,4,6]
print(list(set(l)))
# for i in l:
#     for i2 in l:
#         if l[i2] == i:
#             l.pop(l[i2])
#
# print(l)