def Sum(A,B,C):
    D = A + B + C
    print(D)
Sum(9,7,1)

def total(*args):
    total_var = 0
    for i in args:
        total_var += i
    return total_var

print(total(3,4,5,8,7,23))

def Multiply(*args):
    Total = 1
    for i in args:
        Total *= i
    return Total

numbers = [1,2,3,4]

print(Multiply(*numbers))

def Print(name,*args):
    print(name)
    total = 0
    for i in args:
        total = total + i
    print(total)

Print("Joe John",1,7,1,1)



def Nums(*args):
    Amount = 0
    Total1 = 1
    Total2 = 0
    args_list = list(args)
    for i in args_list:
        Amount = Amount + 1
    if Amount == 1 or Amount == 3 or Amount == 5 or Amount == 7 or Amount == 9 or Amount == 11:

        args_list.append(1)
        Amount = Amount + 1


    for i in range(Amount):
        if i < Amount/2:
            Total1 *= args_list[i]
        else:
            Total2 += args_list[i]
    print(Total1)
    print(Total2)



Nums(1,2,3,4)