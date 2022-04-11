from random import randint
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)
Correct_Number = randint(1,100)
GamePending = True

print("Welcome to the Guessing Game! Pick a number between 1 and 100 and try to guess what i am thinking.")
Difficulty = input("Do you want to do easy or hard mode? ")
Lives = 0
if Difficulty == "easy" or Difficulty == "Easy" or Difficulty == "EASY":
    Lives = 15
    while GamePending != False:
        Number_Input = int(input("Guess the number: "))
        if Number_Input == Correct_Number:
            print("Good job, you won!")
            Retry = input("Do you want to play again? ")
            if Retry == "yes" or Retry == "Yes" or Retry == "YES":
                GamePending = True
                Lives = 15
                Correct_Number = randint(1, 100)
            else:
                GamePending = False
        elif Number_Input > Correct_Number:
            Lives = Lives - 1
            if Lives == 0:
                print("GameOver!")
                Retry = input("Do you want to play again? ")
                if Retry == "yes" or Retry == "Yes" or Retry == "YES":
                    GamePending = True
                    Lives = 15
                    Correct_Number = randint(1, 100)
                else:
                    GamePending = False
            else:
                print(f"To high! You have {Lives} more attempts. Try again!")
        elif Number_Input < Correct_Number:
            Lives = Lives - 1
            if Lives == 0:
                print("GameOver!")
                Retry = input("Do you want to play again? ")
                if Retry == "yes" or Retry == "Yes" or Retry == "YES":
                    GamePending = True
                    Lives = 15
                    Correct_Number = randint(1, 100)
                else:
                    GamePending = False
            else:
                print(f"To low! You have {Lives} more attempts. Try again!")
elif Difficulty == "hard" or Difficulty == "Hard" or Difficulty == "HARD":
    Lives = 10
    while GamePending != False:
        Number_Input = int(input("Guess the number: "))
        if Number_Input == Correct_Number:
            print("Good job, you won!")
            Retry = input("Do you want to play again? ")
            if Retry == "yes" or Retry == "Yes" or Retry == "YES":
                GamePending = True
                Lives = 10
                Correct_Number = randint(1, 100)
            else:
                GamePending = False
        elif Number_Input > Correct_Number:
            Lives = Lives - 1
            if Lives == 0:
                print("GameOver!")
                Retry = input("Do you want to play again? ")
                if Retry == "yes" or Retry == "Yes" or Retry == "YES":
                    GamePending = True
                    Lives = 10
                    Correct_Number = randint(1, 100)
                else:
                    GamePending = False
            else:
                print(f"To high! You have {Lives} more attempts. Try again!")
        elif Number_Input < Correct_Number:
            Lives = Lives - 1
            if Lives == 0:
                print("GameOver!")
                Retry = input("Do you want to play again? ")
                if Retry == "yes" or Retry == "Yes" or Retry == "YES":
                    GamePending = True
                    Lives = 10
                    Correct_Number = randint(1, 100)
                else:
                    GamePending = False
            else:
                print(f"To low! You have {Lives} more attempts. Try again!")