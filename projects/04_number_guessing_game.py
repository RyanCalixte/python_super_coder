# Stage 1
"""
Insert a number between 1 and 10: 12
Not applicable
"""
# NumberQuestion = int(input("Pick a number between 1 and 10: "))
# CorrectNumber = 5

# if NumberQuestion == CorrectNumber:
#     print("You win!")
# elif NumberQuestion > 10 or NumberQuestion < 1:
#     print("Not applicable")
# elif NumberQuestion > CorrectNumber:
#     print("To high")
# elif NumberQuestion < CorrectNumber:
#     print("To low")


# Stage 2









# Stage 3
from random import randint
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")

easy_attempts = 15 #number of lives for easy level
easy_lives = 0
hard_attempts = 10 #number of lives for hard level
hard_lives = 0

play_again = False

while not play_again:
    
    winning_number = randint(1,100)

    DifficultyQuestion = input("Would you like to do easy or hard mode: ")

    Win = False

    if DifficultyQuestion == "hard":
        while not Win:
            NumberQuestion = int(input("Guess the number! "))
            if NumberQuestion == winning_number:
                Win = True
                print("You win!")
                play_again_input = input("Do you want to play the game again [y/n] ? ")
                if play_again_input == "y":
                    play_again = False
                else:
                    play_again = True
            else:
                if hard_attempts == 0:
                    Win = True

                    print("Out of attempts. GAME OVER.")
                    play_again_input = input("Do you want to play the game again [y/n] ? ")
                    if play_again_input == "y":
                        play_again = False
                    else:
                        play_again = True
                elif NumberQuestion > 100 or NumberQuestion < 1:
                    print(f"Not applicable. You have {hard_attempts} more attempts. Try again!")
                elif NumberQuestion > winning_number:
                    print(f"To high. You have {hard_attempts} more attempts. Try again!")
                elif NumberQuestion < winning_number:
                    print(f"To low. You have {hard_attempts} more attempts.Try again!")

                hard_attempts = hard_attempts - 1
                

    if DifficultyQuestion == "easy":
        while not Win:
            NumberQuestion = int(input("Guess the number! "))
            if NumberQuestion == winning_number:
                Win = True
                print("You win!")
                play_again_input = input("Do you want to play the game again [y/n] ? ")
                if play_again_input == "y":
                    play_again = False
                else:
                    play_again = True

            else:
                if easy_attempts == 0:
                    Win = True
                    print("Out of lives. GAME OVER.")
                    play_again_input = input("Do you want to play the game again [y/n] ? ")
                    if play_again_input == "y":
                        play_again = False
                    else:
                        play_again = True
                elif NumberQuestion > 100 or NumberQuestion < 1:
                    print(f"Not applicable. You have {easy_attempts} more attempts. Try again!")
                elif NumberQuestion > winning_number:
                    print(f"To high. You have {easy_attempts} more attempts. Try again!")
                elif NumberQuestion < winning_number:
                    print(f"To low. You have {easy_attempts} more attempts.Try again!")
            

                easy_attempts = easy_attempts - 1