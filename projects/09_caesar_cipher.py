logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
TranslationQuestion = input("Do you want to code or decode a message? ")
LetterAmount = 0

if TranslationQuestion == "code" or TranslationQuestion == "Code" or TranslationQuestion == "CODE":
    Code = input("Insert the text you would like to transfer into code: ")
    ShiftNumber = int(input("Insert the shift number: "))
    coded_stuff = ""
    for i in range(len(Code)):
        for j in range(len(alphabet)):
            if Code[i] == " ":
                coded_stuff = coded_stuff + " "
            elif Code[i] == range(0, 9):
                coded_stuff = coded_stuff + " "
            elif alphabet[j] == Code[i]:
                if j + ShiftNumber >= 26:
                    j = 0
                    ShiftNumber = ShiftNumber - 1
                    coded_stuff = coded_stuff + alphabet[j + ShiftNumber]
                    ShiftNumber = ShiftNumber + 1
                else:
                    coded_stuff = coded_stuff + alphabet[j + ShiftNumber]



    print(f"The coded text is now: {coded_stuff}")
elif TranslationQuestion == "decode" or TranslationQuestion == "Decode" or TranslationQuestion == "DECODE":
    Code = input("Insert the text you would like to decode: ")
    ShiftNumber = int(input("Insert the shift number: "))
    coded_stuff = ""
    for i in range(len(Code)):
        for j in range(len(alphabet)):
            if Code[i] in alphabet:
                if alphabet[j] == Code[i]:
                    if j - ShiftNumber < 0:
                        j = -1
                        ShiftNumber = ShiftNumber - 1
                        coded_stuff = coded_stuff + alphabet[j - ShiftNumber]
                        ShiftNumber = ShiftNumber + 1
                    else:
                        coded_stuff = coded_stuff + alphabet[j - ShiftNumber]
            elif Code[i] == " ":
                coded_stuff = coded_stuff + " "



    print(f"The decoded text is now: {coded_stuff}")


