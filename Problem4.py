"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
def isPalindrome(number):
    reverse = 0
    n = number
    while n != 0:
        reverse = reverse * 10
        reverse = reverse + n % 10
        n = int(n / 10)

    if number == reverse:
        return True
    else:
        return False

product = 0
maxPali = 0
for i in range(1000):
    for j in range(1000):
        product = i * j

        if product > maxPali and isPalindrome(product) == True:
            maxPali = product

print(maxPali)



