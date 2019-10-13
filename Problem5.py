"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

""" BRUTE FORCE
number = 20
while True:
    if number % 11 == 0 and number % 12 == 0 and number % 13 == 0 and number % 14 == 0 and number % 15 == 0 and number % 16 == 0 and number % 17 == 0 and number % 18 == 0 and number % 19 == 0 and number % 20 == 0:
        break;
    number = number + 20
print(number)
"""
def isDivisible(number):
    for i in range(2,21):
        if number % i != 0:
            return False
    return True

number = 20
while True:
    if isDivisible(number) == True:
        break
    number += 20
print(number)
