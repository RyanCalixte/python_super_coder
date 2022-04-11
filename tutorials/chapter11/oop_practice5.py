
class Circle:
    i = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.i += 1

    def area(self):
        area = 3.14 * self.radius * self.radius
        return round(area, 2)

    def circumference(self):
        circumference = 2 * 3.14 * self.radius
        return round(circumference, 2)

    def count_objects(self):
        return f"You have created {Circle.i} objects of the Circle Class."



obj1 = Circle(5)
print(obj1.area())
print(obj1.circumference())

# obj2 = Circle(10)
# print(obj2.area())
# print(obj2.circumference())

print(obj1.count_objects())