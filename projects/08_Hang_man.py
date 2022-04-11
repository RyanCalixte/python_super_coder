import random
import random
from hangman_words import word_list
from hangman_art import logo, stages
#Variables#
LettersCorrect = 0
chosen_word = random.choice(word_list)
Start_Word = chosen_word[0]
End_Word = chosen_word[-1]

LetterAmount = 0

Lives = 6
GamePending = True

i = 0

Word = []  # Is the word that will be displayed

IncorrectWords = []
#Variables#

while Start_Word != End_Word: #Used to check how many letters there are for the chosen word
    Start_Word = chosen_word[LetterAmount]
    LetterAmount = LetterAmount + 1

print(logo)
input("Welcome to Hang man! Are you ready to continue? ")


for i in chosen_word:  # Used to print the blank spaces of the word
    Word.append("_ ")

while GamePending == True:
    LettersCorrect = 0
    i2 = 0
    CorrectLetter = False
    print(stages[Lives])
    print(chosen_word)
    print(f"Correct word: {Word}")
    print(f"Missed letters: {IncorrectWords}")

    Guess_the_word = input("Guess the word, insert a letter: ") #This is the input for the user to type each letter
    print(chosen_word)


    Start_Word = chosen_word[0] #First letter of the Word
    End_Word = chosen_word[-1] #Last letter of the word

    for i2 in range(LetterAmount):  #Used to check if the letter is correct or not
        if chosen_word[i2] == Guess_the_word:
            Word[i2] = Guess_the_word
            CorrectLetter = True

        i2 = i2 + 1
    WordNumber = 0

    for i in range(len(chosen_word)):
        if Word[i] == chosen_word[i]:
            WordNumber = WordNumber + 1
            if WordNumber == LetterAmount:
                print(f"Congragulations, you wont! The word was: {chosen_word}")
                GamePending = False






    if CorrectLetter == False: #Used to take away lives if you are incorrect
        print("Incorrect Letter.")
        Lives = Lives - 1
        IncorrectWords.append(Guess_the_word)



        if Lives == 0: #Used to end the game if all lives are lost

            print(stages[0])
            print(f"You lost all of you lives, GAME OVER. the word was: {chosen_word}")
            GamePending = False


