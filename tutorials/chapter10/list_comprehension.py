# List Comprehension

# Create a list of squares from the numbers 1 to 100

# squares = []
# for i in range(1, 101):
#     squares.append(i * i)
#
# print(squares)

# Append, Loop
# print([i * i for i in range(1, 101)])

# print the numbers from -1 to -10
# -1, -2, -3, -4, ...., -10
# negatives = []
#
# for i in range(1, 11):
#     negatives.append((-i))
#
# print([-i for i in range(1, 11)])

# print the first letter of every element in the list
# names = ["alan", "jack", "ryan", "mark", "steve"]
# ["a", "j", "r", "m", "s"]
# Letters = []
#
# for name in names:
#     Letters.append(name[0])
# print(Letters)
# print([i[0] for i in names])
#
# for i in range(0,5):
#
#     Word = names[i]
#     Letter1 = Word[0]
#     Letters.append(Letter1)
# print(Letters)
#
# print([names[i] for i in range(0,5)])
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for m in numbers:
#     if m % 2 == 0:
#         print(m)

# print([m for m in numbers if m % 2 == 0])

# numbers2 = []
# print(numbers)
# for i in range(0, 10):
#
#     if numbers[i] % 2 == 0:
#         numbers[i] = numbers[i] * numbers[i]
#     else:
#         numbers[i] = numbers[i] - numbers[i] * 2

# print(numbers2)
# for i in range(1, 11):
#     if i % 2 == 0:
#         numbers2.append(i * i)
#     else:
#         numbers2.append(i - i * 2)
# print(numbers2)

# [1,2,3,4,5,6,7,8,9,10] -> [-1,4,-3,16,-5,36,-7,64,-9,100]

# no = [1,2,3,4,5,6,7,8,9,10]
# output = []
# for i in no:
#     if i % 2 == 0:
#         output.append(i**2)
#     else:
#         output.append(-i)
#
# print(output)d
# print([(i**2) if i % 2 == 0 else (-i) for i in no])

# nested List Comprehension
# print a list : [[1,2,3],[1,2,3],[1,2,3]]
output = []
Nums = []
print([[i for i in range(1,4)] for m in range(1,4)])
print([[i*i for i in range(2,5)] for j in range(1,4)])
