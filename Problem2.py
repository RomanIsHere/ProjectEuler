"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
sum = 2
first = 1
second = 2
limit = 4000000
next = 0
i = 0

for i in range(limit):
    if i <= 0:
        next = i
    else:
        next = first + second
        first = second
        second = next
    if next % 2 == 0 and next <= limit:
        sum += next

print(sum)
