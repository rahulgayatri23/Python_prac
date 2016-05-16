from __future__ import print_function
import random
import sys
import os
from datetime import date

threshold = int(raw_input('Enter the threshold : '))

a = [1,3,54,85,98,23,65,3,65,92]
i = 1;
new_a = []

for x in a : 
        if(x < threshold) : 
                new_a.append(x)
for x in new_a : 
        print('new_a[%d] = %d '%(i,x))
        i += 1

