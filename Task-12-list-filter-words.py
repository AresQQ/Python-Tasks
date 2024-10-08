# Create a list that contains 10 words, then create a second list that will contain only those words which have more than 5 letters.
words = ["Elephant" , "Apple" , "Bicycle" , "Mountain" , "Dog" , "Butterfly" , "Table" , "Computer" , "Sun" , "Car"]

more_then_5_letters = []

for word in words:
    if len(word) > 5:
        more_then_5_letters.append(word)

print(more_then_5_letters)