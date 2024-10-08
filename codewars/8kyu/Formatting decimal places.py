#Each number should be formatted that it is rounded to two decimal places.
# You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

def two_decimal_places(x):
    return round(x, 2)

n = 5.5589
a = -3.3424

print(f"{n} is rounded {two_decimal_places(n)}")
print(f"{a} is rounded {two_decimal_places(a)}")