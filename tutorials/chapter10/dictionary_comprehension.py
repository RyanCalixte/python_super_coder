# {1:1, 2:4, 3:9, 4:16, 5:25, ........., 10:100}
print({i:i*i for i in range(1,11)})

Output = {}
name = "Kaustubh Wankhede"

print({i:name.count(i) for i in name})


List = [1,2,3,4,5,6,7,8,9,10]
dict = {}
for i in List:
    if i%2==0:
        dict[i] = "Even"
    else:
        dict[i] = "Odd"
print(dict)

print({i : ("even" if i%2 == 0 else "odd") for i in range(1,11)})

