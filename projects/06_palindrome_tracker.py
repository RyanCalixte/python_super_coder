# kaustubh -> hbutsuak
# dad -> dad

"""
Insert the word : kaustubh
It's not a palindrome

Insert the word : dad
It is a palindrome
"""

WordQuestion = input("Insert a word: ")
ReverseWordQuestion = WordQuestion[-1::-1]
if WordQuestion == ReverseWordQuestion:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")

# Start = WordQuestion[1]
# StartPlus = Start + 1
# StartMinus = Start - 1
# ReversedWordQuestion = WordQuestion
# while Start != WordQuestion[0]:
#     ReversedWordQuestion[Start] = ReversedWordQuestion[StartPlus]
#     Start = Start + 1
#     ReversedWordQuestion[Start] = ReversedWordQuestion[StartMinus]
#
# if WordQuestion == ReversedWordQuestion:
#     print("The word is a palindrome.")
# else:
#     print("The word is not a palindrome.")



