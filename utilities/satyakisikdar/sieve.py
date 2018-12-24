def sieve(lim):
    '''
    returns a list of primes less than the limit lim
    :param lim: the upper bound
    :return: set of primes
    '''
    prime_list = [True for _ in range(lim + 1)]
    primes = set(range(2, lim + 1))  # list of primes

    i = 2
    while i * i < lim:
        j = i ** 2
        while j <= lim:
            prime_list[j] = False  # this is not a prime
            primes.discard(j)
            j += i
        i += 1

    return primes

