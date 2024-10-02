# Obtain three integers from the user and arrange them in order from smallest to largest
# We use int to convert input to integers
n1 = int(input("Podaj pierwszą liczbę całkowitą: "))
n2 = int(input("Podaj drugą liczbę całkowitą: "))
n3 = int(input("Podaj trzecią liczbę całkowitą: "))

numbers = [n1, n2, n3] # Create list

numbers.sort() # list sort default is from lowest to highest

print("Twoje liczby całkowite w kolejności od najmniejszej do największej to:", *numbers)