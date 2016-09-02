import sys
import os

def main() : 
    list1 = [1,2,3,4,5,6,7,99,13,14,56,34,89]
    list2 = [number for number in list1 if number%2==0]

    print (list2)

if __name__ == '__main__' : 
    main()
