#Write a function is_even(number) that accepts a number and returns True if the number is even and False if it is odd.
number = int(input("Podaj liczbę aby sprawdzić czy jest parzysta: "))

def is_even(number):
    if number % 2 == 0:
        return True

    else:
        return False

if is_even(number):
    print("Twoja liczba jest parzysta.")
else:
    print("Twoja liczba jest nieparzysta.")