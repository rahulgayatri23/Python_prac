#Check for palindrome
from __future__ import print_function
import random
import sys
import os
import itertools

list_string = list(raw_input('Give the string to be checked for palindrome : '))
rev_str = str(list_string)[::-1]

if(list_string == rev_str) : 
        print('string %s is a palidrome'%list_string)
else : 
        print('string %s is NOT a palidrome'%list_string)
