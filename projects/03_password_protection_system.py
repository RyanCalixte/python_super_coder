username = "12345"
password = "678910"
email = "yes@gmail.com"
usernamequestion = input("What is your username? ")



passwordquestion = input("What is your password? ")
emailquestion = input("What is your email? ")
if(passwordquestion == password and usernamequestion == username and emailquestion == email):
    print("You successfully logged in!")
else:
    print("Invalid entry!")