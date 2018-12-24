#!/usr/bin/env python
# coding: utf-8

def main():
	N = 4000000;
	sqrt5 = 5**(0.5);
	golden_ratio = (1+sqrt5)/2;

	result = 0
	for n in range(3,100,3):
	    f_n = ((golden_ratio**n-(1-golden_ratio)**n) // sqrt5);
	    if (f_n < N):
	        result += f_n;
	    else:
	        break;

	print(result);


if "__name__" == "__main__":
	main()
