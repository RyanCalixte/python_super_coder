def func(L1):
    p1 = []
    p2 = []

    Even = []
    Odd = []
    EvenOutput = 0
    OddOutput = 1

    StringOutput = []
    for i in L1:
        if type(i) == str:
            p2.append(i)
        elif type(i) == int:
            p1.append(i)
    print(p1)
    print(p2)
    print("-------------------")
    for j in p1:
        if j%2==0:
            Even.append(j)
        else:
            Odd.append(j)
    for i in Even:
        EvenOutput += i
    for i in Odd:
        OddOutput *= i
    print(EvenOutput + OddOutput)
    print("-------------------")
    for i in p2:
        if len(i) == 4:
            uppercase = i.upper()
            lowercase = i[1:].lower()
            new = uppercase[0] + lowercase
            StringOutput.append(new)
        else:
            StringOutput.append(i.upper())
    print(StringOutput)



func([2,3,4,5,"alan","mark",7,9,"him","kau"])