'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from utilities.satyakisikdar import sieve


def main():
    primes = sieve.sieve(10_000_000)
    prime_sum = sum(prime for prime in primes if prime < 2_000_000)
    print(prime_sum)


if __name__ == '__main__':
    main()