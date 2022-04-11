from Coffee_info import MENU, profit, resources


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for i in order_ingredients:
        if resources[i] < order_ingredients[i]:
            print("Insufficient amount of ingredients, please order a different drink or come back later!")

            return False
        else:
            print("The cost of the drink is: ")
            print(drink["cost"])
            return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    total = 0
    quarters_input = int(input("How many quarters?: "))
    quarters_dollar = quarters_input * 0.25
    total += quarters_dollar
    dimes_input = int(input("How many dimes?: "))
    dimes_dollar = dimes_input * 0.1
    total += dimes_dollar
    nickles_input = int(input("How many nickles?: "))
    nickles_dollar = nickles_input * 0.05
    total += nickles_dollar
    pennies_input = int(input("How many pennies?: "))
    pennies_dollar = pennies_input * 0.01
    total += pennies_dollar
    total = round(total, 2)
    print(total)
    if total >= drink["cost"]:
        print(f"You will recieve:")
        Change = round(total - drink["cost"], 2)
        print(Change)
        print("Back.")
    return total



def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if drink_cost > payment:
        print("Payment is not sufficient, please chose a drink that cost less.")
        return False
    else:
        global profit
        profit = profit + drink_cost
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for i in order_ingredients:
        resources[i] = resources[i] - order_ingredients[i]


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):

            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
                print("Order success, Come back next time!")
