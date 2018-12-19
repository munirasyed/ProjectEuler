'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

def is_prime(n):
    '''
    returns True if n is prime
    '''
    if n <= 3:
        return True

    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


def main():
    n = 600_851_475_143

    for k in reversed(range(3, int(sqrt(n)), 2)):  # start from the largest possible factor ie sqrt(n)
        if n % k == 0 and is_prime(k):  # if k divides n and is prime, we have our answer
            print(k)
            break

if __name__ == '__main__':
    main()