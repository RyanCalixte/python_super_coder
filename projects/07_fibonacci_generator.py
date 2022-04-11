"""
Insert how many numbers you want from fibonacci : 6
0
1
1
2
3
5
"""
NumberQuestion = int(input("How many numbers do you want to display?"))
i = 3
NumFib = 1
NumFib2 = 0

print("0")
if NumberQuestion >= 2:
    print("1")
while i <= NumberQuestion:
    print(NumFib + NumFib2)
    NumFib = NumFib + NumFib2
    NumFib2 = NumFib - NumFib2
    i = i + 1

