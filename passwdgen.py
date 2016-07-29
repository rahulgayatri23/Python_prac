from __future__ import print_function
import random
import sys
import os
from datetime import date
import string 

def pwg() : 
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        special = '!@#$%^&*()_+'
        numbers = '1234567890'

        passwd = ''
    
        for i in range(3) : 
                passwd += random.choice(lower)
                passwd += random.choice(upper)
                passwd += random.choice(special)
                passwd += random.choice(numbers)

        return passwd

def passwordGen(digitsInPasswd) : 
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(digitsInPasswd))


def main() : 
        passwd = ''
        passwd = pwg()

        print('your random passwd is %s' %passwd)

        digitsInPasswd = int(raw_input("How many digits do you want in your passwd : "))

        passwd = passwordGen(digitsInPasswd)
        print('your random passwd for %d digits is %s' %(digitsInPasswd,passwd))

if __name__ == '__main__' : 
        main()
