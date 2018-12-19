'''
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

n = 100
sum_sq = n * (n  + 1) * (2*n + 1 ) / 6  # closed form of $\sum_{i} i^2$
sq_sum = (n * (n + 1) / 2) ** 2   # closed form of (\sum_{i} i)^2

print(sq_sum - sum_sq)