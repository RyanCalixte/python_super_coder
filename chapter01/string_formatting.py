firstname = "Ryan"
lastname = "Calixte"
age = "12"

# Output : Hey! I am Ryan Calixte. I am 12 years old.

print("Hey! I am Ryan Calixte. I am 12 years old.")
print("Hey! I am", firstname,lastname,". I am",age,"years old.")

# concatenation -> bad
print("Hey! I am "+firstname+" "+lastname+". I am "+age+" years old.")

# .format() method -> good
print("Hey! I am {} {}. I am {} years old.".format(firstname, lastname, age))

# f string method -> best
print(f"Hey! I am {firstname} {lastname}. I am {age} years old.")