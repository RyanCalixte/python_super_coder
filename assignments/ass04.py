def func(a):
    output = []
    # loop through the input list
    for element in a:
        output.append(element ** 2)
    return output

print(func([1,2,3,4]))