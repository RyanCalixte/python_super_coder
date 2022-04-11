List = ["abc", "tuv", "xyz"]
List2 = []
i = 0
def Reverse():
    for i in range(3):
        ListValue = List[i]
        List2.append(ListValue[::-1])
        i = i + 1

    print(List2)

Reverse()

