# -*- coding: utf-8 -*-

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import math

def is_palindrome(x): #this solution avoids O(n) space requirement when converting int to string and reversing it
    #return true if input is palindrome in O(n) time and O(1) space.
    if x <= 0: #sanity check
        return False
    num_digits = math.floor(math.log10(x))+1 #get number of digits by taking log10 of the number +1
    msd_mask = 10**(num_digits-1) #most significant digit is x // msd_mask
    for i in range(num_digits//2):
        if x // msd_mask != x%10: #if most significant digit != least significant digit
            return False
        x %= msd_mask #remove most significant digit of x
        x //=10 #remove least significant digit of x
        msd_mask //=100 #update msd_mask because we removed the msd and lsd
    return True

def brute_force(): #return largest palindrome product in O(n^2) time and O(1) space.
    largest=0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if is_palindrome(i*j):
                #print(i, j)
                if i*j>largest:
                    largest=i*j
                    #print(i, j)
    return  largest

def get_product(): #This is still O(n^2) time but requires lesser checks
    """
    The palindrome will be 6 digits abccba. So the palindrome is divisible by 11 (property). Long derivation below.
    abbca = 11 * some number = x1 * x2 => either x1 or x2 is divisible by 11.
    i.e. 100000a + 10000b + 1000c + 100c + 10b + a = x1 * x2, where x1 and x2 are the 3 digit numbers.
    => 100001a + 10010b + 1100c = x1 * x2
    => 11(9091a + 910b + 100c) = x1 * x2 
    Another solution would be to directly calculate a, b, and c.
    """
    largest=0
    for i in range(999, 100, -1):
        for j in range(990, 100, -11): #990 is the largest number divisible by 11
            if is_palindrome(i*j):
                #print(i, j)
                
                if i*j>largest:
                    largest=i*j
                    #print(i, j)
    return  largest
            
def main():
    print(get_product())
            
if __name__ == '__main__':
    main()