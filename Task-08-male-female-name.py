#Write a program that checks whether a given name is male or female (assume that female names end with the letter "a").

name = input("Podaj imie: ")
name = name.lower() # Convert all letters to lowercase to handle uppercase letters.

if name.endswith("a"):
    print("Jest to imię żeńskie. ")
else:
    print("Jest to imię męskie.")
