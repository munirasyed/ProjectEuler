'''
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''


fib_n1 = 2  # stores fib(n - 1)
fib_n2 = 1  # stores fib(n - 2)
even_sum = 2  # sum of even terms - initially it is 2

while True:
    fib_n = fib_n1 + fib_n2  # compute fib(n)
    if fib_n > 4_000_000:  # break if fib(n) > 4M
        break

    if fib_n % 2 == 0:   # add to the even sum if fib(n) is even
        even_sum += fib_n

    fib_n2 = fib_n1  # updation - fib(n - 1) becomes fib(n - 2)
    fib_n1 = fib_n  # fib(n) becomes fib(n - 1)

print(even_sum)
