from calculator_art import logo

print(logo)
print("Welcome to the calculator!")

def NewCalculation():
    Calculation = 0
    Samecalc = False
    while True:
        if Samecalc is True:
            FirstNumber = Calculation
        else:
            FirstNumber = int(input("What's the first number?: "))

        Operaters = ["+", "-", "*", "/"]
        for i in range(4):
            print(Operaters[i])

        Operation = input("Pick an operation: ")
        SecondNumber = int(input("What's the second number?: "))
        if Operation == "+":
            Calculation = FirstNumber + SecondNumber
            print(f"{FirstNumber} + {SecondNumber} = {Calculation}")
        elif Operation == "-":
            Calculation = FirstNumber - SecondNumber
            print(f"{FirstNumber} - {SecondNumber} = {Calculation}")
        elif Operation == "*":
            Calculation = FirstNumber * SecondNumber
            print(f"{FirstNumber} * {SecondNumber} = {Calculation}")
        elif Operation == "/":
            Calculation = FirstNumber / SecondNumber
            print(f"{FirstNumber} / {SecondNumber} = {Calculation}")

        SameNumberQuestion = input(f"Type 'y' to continue calculation with {Calculation}, or type 'n' to start a new calculation: ")
        if SameNumberQuestion == "y":
            Samecalc = True
        if SameNumberQuestion == "n":
            Samecalc = False

NewCalculation()

