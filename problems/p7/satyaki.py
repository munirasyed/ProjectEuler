'''
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
from utilities.satyakisikdar.sieve import sieve

def main():
    lim = 200_000
    primes = list(sieve(lim))
    print('10_001st prime:', primes[10_000])

if __name__ == '__main__':
    main()