def Function(L1,L2):
    new_list = []
    for i in L1:
        for K in L2:
            if i == K:
                new_list.append(i)

    print(new_list)



Function([1,2,5,8],[1,2,7,6])