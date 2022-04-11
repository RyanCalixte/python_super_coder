name = input("Insert your name : ")

i = 0
while i < len(name):
    print(f"{name[i]} : {name.count(name[i])}")
    i  = i + 1

var = "Ryan Calixte"
print(var.count("a"))
