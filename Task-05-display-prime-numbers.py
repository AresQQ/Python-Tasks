#Write a program that displays prime numbers from 1 to 100

#Range must end on 101 because the right one is not closed we start from 2 as we want prime numbers only
for a in range(2, 101):
    prime = True

    #prime check
    for b in range(2, a):
        if a % b == 0:
            prime = False
            break

    #returning only prime numbers in our range
    if prime:
        print(a)