"""

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""


# the sum of the first 100 numbers squared
import math
sumOfSquaredNumbers = 0
sumOfNumbers = 0

for i in range(1,101):
    sumOfSquaredNumbers += math.pow(i,2)
    sumOfNumbers += i


difference = math.pow(sumOfNumbers,2) - sumOfSquaredNumbers

print(difference)


