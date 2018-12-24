#!/usr/bin/env python
# coding: utf-8

# closed-form Fibonnaci function
def cf_fibonnaci(n):
    sqrt5 = 5**(0.5);
    return int((1/sqrt5)*(((1+sqrt5)/2)**n - ((1-sqrt5)/2)**n))

def main():
	N = 4*(10**6) #upper-bound 4M

	result = 0
	for n in range(3,100,3):
	    f_n = cf_fibonnaci(n);
	    print(f_n)
	    if (f_n < N):
	        result += f_n;
	    else:
	        break;
	print(result)


if "__name__" == "__main__":
	main()