# Some more methods to add stuff to a list :
# insert
# extend

fruits1 = ["mango", "orange", "watermelon"]

# .insert() method -> It adds data to the list at the index which we provide.
print(fruits1)
fruits1.insert(1, "apple")
print(fruits1)

# .extend() method -> It fetches all the elements from the first list and then it extends itself with another list.
cars = ["Rolls Royce", "BMW", "Porsche", "Audi"]
cars2 = ["Vitara Brezza", "XUV 700", "WAGNOR", "Honda City"]
cars.extend(cars2)

print(cars)