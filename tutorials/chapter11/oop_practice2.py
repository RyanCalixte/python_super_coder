class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Buss(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def Introduction(self):
        print(f"The name of this vehicle is a {self.name} It can go to up to {self.max_speed} and has a mileage of {self.mileage}")

Ob1 = Buss("Buss", "50 mph", "15wdfs")
Ob1.Introduction()
