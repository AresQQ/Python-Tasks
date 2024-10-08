#Create a dictionary that will store information about countries and their capitals.
#Add 5 elements to it, and display the data from the dictionary in the format Country - Capital.

countries_and_capitals = {
    "Polska": "Warszawa",
    "Niemcy": "Berlin",
    "Francja": "Paryż",
    "Hiszpania": "Madryt",
    "Włochy": "Rzym",
}

for country, capital in countries_and_capitals.items():
    print(f"{country} - {capital}")

