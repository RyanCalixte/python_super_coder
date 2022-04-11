# OOP -> Object Oriented Programming
# Object Oriented Programming is just a style of writing code.
# We create classes in OOP. Classes are just blueprint.

class Car:
    def __init__(self, name, model, manufacturer, price, life):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.price = price
        self.life = life

    # function inside a class its called as a method
    def introduce_yourself(self):
        print(f"I am {self.name}. My technical name is {self.model}. I was manufactured by {self.manufacturer}. I "
              f"will be sold at ${self.price}. I will die in the next {self.life} years.")


obj1 = Car("BMW", "BMW AS-78", "TATA", "8500000", "8")
obj1.introduce_yourself()


# class called as Person
# Attributes -> first_name, last_name, age, email, education, job
# Methods -> introduce_yourself, check_if_18



class Person:
    def __init__(self, First_name, Last_name, Age, Email, Education, Job):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age
        self.Email = Email
        self.Education = Education
        self.Job = Job

    def Introduction(self):
        print(f"Hello, My name is {self.First_name} {self.Last_name}. "
              f"I am {self.Age} years old and my Email is {self.Email}."
              f" I used to go to school at {self.Education} and i currently work at {self.Job}")

    def check_if_18(self):
        if self.Age >= 18:
            print("You are eligable for voting")
        else:
            print("You are eligable for voting")



Values = Person("Ryan","Calixte","12","sadasd@asdasf","asfafasad","bfssg")
Values.Introduction()



# class Phone
# Attributes -> name, model, manufacturer, price, memory, front_camera_mp, rear_camera_mp
# Methods -> Introduce_yourself
class Phone:
    def __init__(self, Name, Model, Manufacturer, Price, Memory, Front_camera_mp, Rear_camera_mp):
        self.Name = Name
        self.Model = Model
        self.Manufacturer = Manufacturer
        self.Price = Price
        self.Memory = Memory
        self.Front_camera_mp = Front_camera_mp
        self.Rear_Camera_mp = Rear_camera_mp
    def Introduction(self):
        print(f"This phone is named {self.Name}. Its model is: {self.Model} and {self.Manufacturer} is its Manufacturer. It cost a total of ${self.Price} and has {self.Memory} Memory. Its front camera mp is {self.Front_camera_mp} and its rear camera mp is {self.Rear_Camera_mp}")

Printing = Phone("Apple", "Apple2", "Apple3","Apple4","Apple5","Apple6","Apple7")
Printing.Introduction()