from __future__ import print_function
import sys
import os
import math

def isPrime(num) : 
        for j in range (2,num) : 
                if (num % j) == 0 : 
                        return 0
        
        return 1


def primeNumGen(numbers) :

        fp = open('primeNum.txt' , 'w')
        for i in range (2, numbers) :
                if(isPrime(i)) :
                        fp.write(str(i))
                        fp.write('\n')

        fp.close()


def isHappy(num) : 
        
        if num == 1 : 
                return 0

        visited = set()
        sums = num
        
        while sums!=1 : 
                if sums in visited : 
                        break
                visited.add(sums)
                sumsStr = str(sums)
                index = 0
                sumsN = 0
                for i in range (0, len(sumsStr)) : 
                        sumsN = sumsN + int(sumsStr[index]) * int(sumsStr[index])
                        index+=1

                sums = sumsN

        if sums == 1 : 
                return 1
        else : 
                return 0

def happyNumbers(numbers) : 

        fp = open('happyNum.txt' , 'w')
        for i in range (1, numbers) : 
                if(isHappy(i)) : 
                        fp.write(str(i))
                        fp.write('\n')
        fp.close

def checkOverlap() : 
        #list of elements in prime number file
        with open('primeNum.txt', 'r') as fp1: 
                primeNumSet = set(list(fp1))

        #list of elements in happy number file
        with open('happyNum.txt', 'r') as fp2: 
                happyNumSet = set(list(fp2))

        overLap = primeNumSet.intersection(happyNumSet)

        with open('overLap.txt', 'w') as fp3: 
                for x in overLap : 
                        fp3.write(x)

        fp1.close()
        fp2.close()
        fp3.close()


def main():

        numbers = 100

        #generate prime numbers 
        primeNumGen(numbers)

        #generate happy numbers
        happyNumbers(numbers)

        #check for overlap among prime and happy numbers
        checkOverlap()

if __name__ == '__main__' : 
        main()
