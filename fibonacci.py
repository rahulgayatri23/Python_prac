#Check for palindrome
from __future__ import print_function
import random
import sys
import os
import itertools

fib_int = int(raw_input('Fibonacci series till : '))

element1 = 1
element2 = 1
print('The numbers in the fibonaci series are as follows' )
print('%d %d '%(element1, element2), end="")

for x in range(2, fib_int) : 
        print ('%d ' %(element2 + element1), end="")
        tmp = element1
        element1 = element2
        element2 = tmp + element2

print('\n')       
