from random import randint
logo = """

.------.            _     _            _    _            _   

|A_  _ |.          | |   | |          | |  (_)          | |  

|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __

| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /

|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <

`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_

      |  \/ K|                            _/ |               

      `------'                           |__/          

"""

Money = 1000
print(logo)
print("Welcome to black jack!")
print(f"You have a total of ${Money}!")
Gameprogress = True
GameStop = False
while Gameprogress == True:
    RandomNum1 = randint(1, 11)
    RandomNum2 = randint(1, 11)
    RandomNum3 = randint(1, 11)
    Total = RandomNum1 + RandomNum2
    Dealers_JackAmount = []
    Player_JackAmount = []
    Player_JackAmount.append(f"{RandomNum1}, {RandomNum2}")
    Dealers_JackAmount.append(f"{RandomNum3}")
    Player_Total = Total
    Dealers_Total = Dealers_JackAmount
    BettingAmount = int(input("How much money are you willing to bet? "))
    while BettingAmount > Money:
        print("Insert an amount that you have.")
        BettingAmount = int(input("How much money are you willing to bet? "))
    GameStop = False
    while GameStop == False:
        print("Player     Dealer")
        print(f"   {Player_JackAmount}     {Dealers_JackAmount}")
        print(f"   {Player_Total}     {Dealers_Total}")
        Player_Turn = True
        Dealer_Turn = False


        while Player_Turn == True:
            Hit_Stand = input("Do you want to HIT or STAND?")

            ChosenNumber1 = randint(1, 11)

            if Hit_Stand == "hit" or Hit_Stand == "Hit" or Hit_Stand == "HIT":
                Player_JackAmount = Player_JackAmount + ChosenNumber1
                print(f"You gained {ChosenNumber1} giving you a total of {Player_JackAmount}.")
            elif Hit_Stand == "stand" or Hit_Stand == "Stand" or Hit_Stand == "STAND":
                Player_Turn = False

            if Player_JackAmount > 21:
                Money = Money - BettingAmount

                if Money <= 0:
                    print("You lost all of your money, GAMEOVER.")
                    Gameprogress = False
                else:

                    GameStop = True
                    print(f"You lose! You lost a total of {BettingAmount}. You currently have {Money}")
        Dealer_Turn = True
        while Dealer_Turn == True:
            ChosenNumber2 = randint(1, 11)




