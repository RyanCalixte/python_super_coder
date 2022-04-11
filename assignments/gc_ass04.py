List1 = [1,2,5,8]
List2 = [1,2,7,6]
ListChecked = []
i = 0
def Switch():
    for i in range(3):
        if List1[i] == List2[i]:
            ListChecked.append(List1[i])
        i = i + 1
    print(ListChecked)

Switch()