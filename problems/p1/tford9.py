#!/usr/bin/env python
# coding: utf-8

import math as m, numpy as np;

x = 3; y = 5; n = 1000;

upper_bound_x_multiplier, x_multiplier_remainder  = divmod(n,x);
upper_bound_y_multiplier, y_multiplier_remainder = divmod(n,y);
upper_bound_xy_multiplier, xy_multiplier_remainder = divmod(n,(x*y));

if not x_multiplier_remainder:
    upper_bound_x_multiplier = upper_bound_x_multiplier - 1;
if not y_multiplier_remainder:
    upper_bound_y_multiplier = upper_bound_y_multiplier - 1;
if not xy_multiplier_remainder:
    upper_bound_xy_multiplier = upper_bound_xy_multiplier - 1;

result = sum ([ x*(idx) for idx in range(upper_bound_x_multiplier+1) ]);
result += sum ([ y*(idx) for idx in range(upper_bound_y_multiplier+1) ]);
result -= sum ([ x*y*(idx) for idx in range(upper_bound_xy_multiplier+1) ]);

print(result);




