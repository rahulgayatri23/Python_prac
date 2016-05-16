from __future__ import print_function
import random
import sys
import os
from datetime import date

def main() : 
        a = [12, 34, 54, 1, 93, 22, 44, 81, 88]
        b = [1, 2, 43, 54, 92, 81, 19]

        for x in a : 
                if(x in b) : 
                        print(x)

if __name__ == '__main__' : 
        main()
