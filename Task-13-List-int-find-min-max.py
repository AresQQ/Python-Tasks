#Create a list filled with ten integers. Find the smallest and largest number.
numbers = [5, 12, 8, 3, 15, 7, 22, 1, 9, 14]

#print("Najmiejsza liczba to:",min(numbers))
#print("Najwieksza liczba to:",max(numbers))

smallest = numbers[0]
largest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

    if number > largest:
        largest = number

print(f"Największa liczba to: {largest}")
print(f"Najmniejsza liczba to: {smallest}")