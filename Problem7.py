"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
from math import ceil


def isPrime(number):
    top = ceil(number ** 0.5) + 1
    for i in range(3,top,2):
        if number % i == 0:
            return False
    return True

number = 1
count = 1
limit = 10001
highestPrime = 0

while count <= limit:
    if isPrime(number) == True:
        count += 1
        highestPrime = number

    number += 2

print(highestPrime)
