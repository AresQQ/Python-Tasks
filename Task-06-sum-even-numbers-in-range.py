# Write a program that will display the sum of all even numbers in the range 1 - 100.

sum = 0

for a in range(1, 101):
    if a % 2 == 0:
        sum += a

print(sum)