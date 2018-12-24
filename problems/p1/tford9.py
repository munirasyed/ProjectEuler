#!/usr/bin/env python
# coding: utf-8

x = 3; y = 5; n = 1000;
xy = x*y;
n -= 1;

upper_bound_x_multiplier  = int(n/x);
result  = sum ([ x*(idx) for idx in range(1,upper_bound_x_multiplier+1)]);
upper_bound_y_multiplier  = int(n/y);
result += sum ([ y*(idx) for idx in range(1,upper_bound_y_multiplier+1)]);
upper_bound_xy_multiplier = int(n/(xy));
result -= sum ([ xy*(idx) for idx in range(1,upper_bound_xy_multiplier+1)]);

print(result);




