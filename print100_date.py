from __future__ import print_function
import random
import sys
import os
from datetime import date

ip_name = raw_input("What is your name : ")
current_year = date.today().year

while(ip_name != 'Q') : 
        current_age = raw_input ('What is your age : ')
        year_100 = str(current_year + (100 - int(current_age)))
        print(ip_name + ' will be 100 in the year ' + year_100)
        ip_name = raw_input("What is your name : ")
