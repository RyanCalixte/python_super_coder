class MoneyMachine:

    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Profit: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        "Returns the total calculated from coins inserted."
        Total = 0

        ProccessedQuarters = int(input("How many quarters do you have?: "))
        ProccessedQuarters = ProccessedQuarters * .25
        Total = Total + ProccessedQuarters

        ProccessedDimes= int(input("How many dimes do you have?: "))
        ProccessedDimes = ProccessedDimes * .10
        Total = Total + ProccessedDimes

        ProccessedNickles = int(input("How many nickels do you have?: "))
        ProccessedNickles = ProccessedNickles * .05
        Total = Total + ProccessedNickles

        ProccessedPennies = int(input("How many pennies do you have?: "))
        ProccessedPennies = ProccessedPennies * .01
        Total = Total + ProccessedPennies
        return Total






    def make_payment(self, cost):
        "Returns True when payment is accepted or False if insufficient. If payment is more, it will return the change as well"
        TakenMoney = self.process_coins()
        if TakenMoney < cost:
            return False
        else:
            Returnedmoney = TakenMoney - cost


