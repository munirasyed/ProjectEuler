'''
Largest exponential
Problem 99
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''
import math

c = 632382; d = 518061
a = 519432; b = 525806

print(b - d * math.log(c, a))

with open('./base_exp.txt') as f:
    max_line = -1
    max_a = 2
    max_b = 2
    for i, line in enumerate(f.readlines()):
        c, d = map(int, line.split(','))
        if max_b - d * math.log(c, max_a) < 0:
            max_a = c
            max_b = d
            max_line = i + 1
    print(max_a, max_b, max_line)