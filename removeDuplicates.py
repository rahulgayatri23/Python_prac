from __future__ import print_function
import random
import sys
import os
from datetime import date

names = ["rahul", "prem", "mahesh", "prathyu", "rahul", "sujana", "srilatha", "prathyu" ]
newNames = []

print ('removing duplicates from the list')
for x in names : 
        if x in newNames : 
                pass
        else : 
                newNames.append(x)

for x in newNames : 
        print(x)

nameSet = set(names)

print ('\n removing duplicates using the set method')

for x in nameSet : 
        print( x )


