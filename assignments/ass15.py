def Transfer(power, *args):
    NumMultiplied = []
    if len(args) == 0:
        print("There wasn't any inserted value.")
    else:
        for i in args:
            NumMultiplied.append(i ** power)
        print(NumMultiplied)


nums = [1, 2, 3, 4]
Transfer(2, *nums)
