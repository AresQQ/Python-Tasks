#Write a function factorial(n) that takes an integer n and returns its factorial (n!).
n = int(input("Podaj liczbe oby obliczyć jej silnie: "))

def factorial(n):
    result = 1
    for x in range(2, n + 1):
        result *= x
    return result

print(factorial(n))









