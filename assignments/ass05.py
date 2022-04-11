"""
Insert the name : Kaustubh
K : 1
a : 1
u : 2
s : 1
t : 1
u : 2
b : 1
h : 1
"""
Check = False
CheckLetterNum = 1
NameQuestion = input("What is your name?")
NumberSaved1 = 1
NumberSaved2 = 1
NumberSaved3 = 1
NumberSaved4 = 1
NumberSaved5 = 1
NumberSaved7 = 1
NumberSaved8 = 1
NumberSaved9 = 1
NumberSaved10 = 1
while not Check:

    NameQuestion[CheckLetterNum]
    CheckLetterNow = NameQuestion[CheckLetterNum]
    while CheckLetterNum > 1:
        CheckLetterNum = CheckLetterNum - 1
        CheckLetterBefore = NameQuestion[CheckLetterNum]
        if CheckLetterBefore == CheckLetterNow:
            NumberSaved1 = NumberSaved1 + 1

    CheckLetterNum = CheckLetterNum + 2
