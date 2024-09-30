#Write a program that checks whether the number entered by the user is greater than 0, less than 0 or equal to 0
try:

#Retrieving data from the user
    number = float(input("Podaj liczbę "))

#Check if a number is an integer
    if number.is_integer():
        number = int(number)

#Check if number is equal, less or greater then 0
        if number == 0:
            print(f"Number {number} is equal 0")
        elif number < 0:
            print(f"Number {number} is less then 0")
        else:
            print(f"Number {number} is greater  then 0")

    else:
        print(f"number {number} is not an integer!")

# Error when the user provides something other than a number
except ValueError:
    print("The value entered is not a number! Please enter the correct number.")