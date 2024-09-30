# Write a program that checks whether the number entered by the user is even or odd

try:

    #Retrieving data from the user
    number = float(input("Enter a number to check whether it is even or odd "))

    #Check if a number is an integer
    if number.is_integer():
        number = int(number)
        #Check if the number is even
        if number % 2 == 0:
            print(f"Number{number} is even")
        else:
            print(f"Number{number} is odd")
    else:
        print("The given number is not an integer!")

# Error when the user provides something other than a number
except ValueError:
    print("The value entered is not a number! Please enter the correct number.")

        