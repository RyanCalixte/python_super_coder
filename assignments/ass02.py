# Grade Calculator

"""
The computer will ask you to insert your marks in these particular subject.

English : 85
Hindi : 82
Marathi : 89
Sanskrit : 96
Algebra : 100
Geometry : 92
Physics : 100
Chemistry : 87
Biology : 64
History : 95
Geography : 98
IT : 100
Games : 95

Total Marks out of 1183 / 1300.
The percentage you gained is 91%.
"""
EnglishScore = int(input("What is your English Score?"))
HindiScore = int(input("What is your Hindi Score?"))
MarathiScore = int(input("What is your Marathi Score?"))
SanskritScore = int(input("What is your Sanskrit Score?"))
AlgebraScore = int(input("What is your Algebra Score?"))
GeometryScore = int(input("What is your Geometry Score?"))
PhysicsScore = int(input("What is your Physics Score?"))
ChemistryScore = int(input("What is your Chemistry Score?"))
BiologyScore = int(input("What is your Biology Score?"))
HistoryScore = int(input("What is your History Score?"))
GeographyScore = int(input("What is your Geography Score?"))
ITScore = int(input("What is your IT Score?"))
GamesScore = int(input("What is your Games Score?"))

Total = EnglishScore + HindiScore + MarathiScore + SanskritScore + AlgebraScore + GeographyScore + PhysicsScore + ChemistryScore + BiologyScore + HistoryScore + GeometryScore + ITScore + GamesScore
print(f"Your total score is {Total} / 1300")
Accuracy = round(Total/1300 * 100, 2)
print(f"The percentage : {Accuracy} ")
