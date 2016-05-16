from __future__ import print_function
import random
import sys
import os
from datetime import date

number = int(raw_input('Give the number : '))
divisors_list = []

for x in range (1, number) : 
        if(number%x == 0) :
                divisors_list.append(x)

for x in divisors_list : 
        print(x)


