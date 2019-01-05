# -*- coding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import gcd

def get_lcm():
    lcm = 1
    for i in range(2, 21):
        #print(i, gcd(int(lcm), i))
        lcm = int(lcm*i/gcd(lcm, i))
    return(lcm)

def main():
    print(get_lcm())
            
if __name__ == '__main__':
    main()