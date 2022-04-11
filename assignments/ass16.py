def Capitalize(*args):
    for i in args:
        UppercaseLetter = i[0].upper()
        LowercaseLetter = i[1:]
        UppercaseLetter.capitalize()
        print(UppercaseLetter + LowercaseLetter)

Capitalize("ryan","kaustubh","jacob")