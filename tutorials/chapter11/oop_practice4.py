class Shape:
    def __init__(self, close_open, sides, angles, corners):
        self.close_open = close_open
        self.sides = sides
        self.angles = angles
        self.corners = corners
    def introduction(self):
        print(f"This shape can {self.close_open}. It has {self.sides} and {self.corners} and {self.angles} angles. ")

class Quadrilateral(Shape):
    def __init__(self, close_open, sides, angles, corners, property1, property2):
        super().__init__(close_open, sides, angles, corners)
        self.property1 = property1
        self.property2 = property2
    def introduction2(self):
        print(f"Its first property is {self.property1} and the second is {self.property2}.")

class Square(Quadrilateral):
    def __init__(self, close_open, sides, angles, corners, property1, property2, length, breadth, area, perimeter, prop1, prop2):
        super().__init__(close_open, sides, angles, corners, property1, property2)
        self.length = length
        self.breath = breadth
        self.area = area
        self.perimeter = perimeter
        self.prop1 = prop1
        self.prop2 = prop2
    def introduction3(self):
        print(f"It has a length of {self.length} and a breadth of {self.breath} so it has an area of {self.area}. Its perimeter is {self.perimeter} and its first property is {self.prop1} and its second is {self.prop2}")

obj1 = Shape("close", "4", "4", "4")
obj2 = Quadrilateral("close", "4", "4", "4", "asdas", "asfdsfds")
obj3 = Square("close", "4", "4", "4", "asdas", "asfdsfds", "close", "4", "4", "4", "asdas", "asfdsfds")
obj1.introduction()
obj2.introduction2()
obj3.introduction3()