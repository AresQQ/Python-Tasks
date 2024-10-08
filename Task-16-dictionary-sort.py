#sort dictionary alphabetic
from itertools import count

countries_and_capitals = {
    "Polska": "Warszawa",
    "Niemcy": "Berlin",
    "Francja": "Paryż",
    "Hiszpania": "Madryt",
    "Włochy": "Rzym",
}

countries_and_capitals = dict(sorted(countries_and_capitals.items()))

for country, capital in countries_and_capitals.items():
    print(f"{country} - {capital}")