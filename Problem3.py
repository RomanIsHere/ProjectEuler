"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

number = 600851475143
#number = 100
highestFactor = 0
i = 3
while number != 1:
    while number % i == 0:
        number = number / i
        highestFactor = i
    i = i + 2



print(highestFactor)
