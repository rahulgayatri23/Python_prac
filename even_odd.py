from __future__ import print_function
import random
import sys
import os
from datetime import date

num = int(raw_input('Give a numerator : '))
check = int(raw_input('Give a denominator : '))

if((num%check) == 0) : 
        print(' Perfect division ')
else : 
        print(' Reaminder is ', num%check)
