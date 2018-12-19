'''
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_nk(n, k):
    '''
    Finds the sum of numbers less than n that are a multiple of k
    :return: the closed form of the sum $k * \sigma_{i=1}^{n // k} i$
    '''
    k1 = n // k
    return k * (k1 * (k1 + 1)) / 2

def main():
    n = 1000  # the n we want
    n -= 1  # the result does not include n
    # add the numbers that are multiples of 3 and 5 and take away the ones that are a multiple of 15
    result = sum_nk(n, 3) + sum_nk(n, 5) - sum_nk(n, 15)
    print(result)

if __name__ == '__main__':
    main()