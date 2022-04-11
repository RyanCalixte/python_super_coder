def Return(*args):
    Output = []
    for i in args:
        if type(i) == int or type(i) == float:
            Output.append(i)
    print(Output)


Return("True","False",[1,2,3],1,1.0,3)