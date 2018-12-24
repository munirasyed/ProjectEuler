import math as m;
import numpy as np;

x = 3;
y = 5;

n = 10;

upper_bound_x_multiplier = m.floor(x/n);
upper_bound_y_multiplier = m.floor(y/n);

x_multiples = [];
y_multiples = [];

for i in range(upper_bound_x_multiplier):
