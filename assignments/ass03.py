"""
Insert the length : 2500
Insert the breadth : 2000
DO you want to go for area or perimeter [ a / p ] : a

"""

# formula :
# area -> lxb
# perimeter -> 2*(l+b)

Length = int(input("What length do you want to chose: "))
Width = int(input("What Width do you want to chose: "))
Question = input("Do you want ot find the area or perimeter? [ a / p ]:")
Area = Length*Width
Perimeter = 2*Length + 2*Width
if Question == "a" or Question == "A" or Question == "area" or Question == "Area" or Question == "AREA":
    print(f"The area is: {Area}")
elif Question == "p" or Question == "P" or Question == "perimeter" or Question == "Perimeter" or Question == "PERIMETER":
    print(f"The perimeter is: {Perimeter}")

