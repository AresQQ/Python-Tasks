#Write a program that show you your grade from your points range 1-100.
#Retrieving data from the user
score = int(input("Enter your points to receive your grade "))

#Check the score range to get a grade. Starting from the lowest as when it reach the score point it will stop.
if score < 60:
    print("Your grade is 1")
elif score < 70:
    print("Your grade is 2")
elif score < 80:
    print("Your grade is 3")
elif score < 90:
    print("Your grade is 4")
elif score <= 100:
    print("Your grade is 5")
else:
    print("Please put score from 0 to 100") 