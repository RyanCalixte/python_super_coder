def Reverse(*args):
    Output = []
    for i in args:
        Output.append(i[::-1])
    print(Output)

Reverse("abc","tuv","xyz")