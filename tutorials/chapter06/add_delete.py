user_info = {
    "First_Name": "Ryan",
    "Last_Name": "Calixte",
    "Age": "12",
    "Email": "zenakustsu123890@gmail.com",
    "Adress": "gdsfjkssdhffjsk nw road asdfjsdfj"

}

user_info["Phone_Number"] = "954 304 5712"
print(user_info["Phone_Number"])

user_info.popitem()

user_info.pop("Age")
print(user_info)