# Create a game in which a number between 1 and 100 is randomly selected and stored in a variable. Then, ask the user to guess this number.
# After each attempt, display information indicating whether the user's guess is smaller or larger than the randomly selected number.
# When the user guesses the number, end the game.

import random

#Generate random number between 1 and 100.
random_number = random.randint(1,100)
user_number = None

while True:  # Loop runs until met break condition.
    user_number = int(input("Podaj liczbę: "))

    #Check if the user's number is smaller than the random number and return hint or end the loop on right guess.
    if user_number < random_number:
        print("Twoja liczba jest mniejsza od naszej spróbuj jeszce raz")
    elif user_number > random_number:
        print("Twoja liczba jest wiekszą od naszej")
    else:
        print("Brawo zgadłeś!")
        break
