# Create a list that contains 10 words, then create a second list that will contain only those words which have more than 5 letters.
list = ["Elephant" , "Apple" , "Bicycle" , "Mountain" , "Dog" , "Butterfly" , "Table" , "Computer" , "Sun" , "Car"]
long_list = [word for word in list if len(word) >5]

print(long_list)