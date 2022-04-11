class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 350,
            "milk": 250,
            "coffee": 150
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")


    def is_resource_sufficient(self, drink):
        """Returns True when order can be made. False if ingredients are insufficient."""
        for i in drink.ingredients:
            if self.resources[i] < drink[i]:
                print(f"Sorry there is not enough {i}")
                return False
            else:
                return True


    def make_coffee(self, order):
        """Deducts the required ingredients from the resources and Prints out the final output."""
        for i in order.ingredients:
            self.resources[i] -= order.ingredients[i]
        print(f"Your {order} is finished, Enjoy ☕!")



