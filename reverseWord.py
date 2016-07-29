from __future__ import print_function
import random
import sys
import os
from datetime import date


def reverseString(string) : 
        splitString = string.split()
        reverseStringList = []
        for i in reversed(splitString) : 
                reverseStringList.append(i)
                reverseStringList.append( ' ')
      
        reverseString = ''.join(reverseStringList)
        
        return (reverseString)

def main() : 
        #ask the user to pass a string
        testString = raw_input('Enter the string to be reversed : ')
        print ('The string passed is \n "%s"' %testString)

        #reverse the string in this function and print it
        rString = reverseString(testString)
        print ('The reverse string is \n "%s"' %rString)

if __name__ == '__main__' : 
        main()
