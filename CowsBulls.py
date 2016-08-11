from __future__ import print_function
import random
import sys
import os
from datetime import date


def CowOrBull(randomNum, letter) :
        i = 0
        numBulls = 0
        numCows = 0

        for x in letter :
                if x in randomNum and randomNum[i] == x : 
                        numBulls+=1
                else :
                        if x in randomNum : 
                                numCows+=1
                i+=1

        if numBulls==0 and numCows==0 : 
                print("SORRY : Neither Cow nor Bull")
        else : 
                print('Num of Bulls = %d\t Num of Cows = %d'%(numBulls,numCows))

        return numBulls

def main() : 
        #Generate a 4 digit random numberd
        numbers = '123467890'
        randomNum = str(random.randint(0,9999))
        print ('randInt = %s'%randomNum)

        bullsFound = 0

        print ("\t\tCow and Bulls Game")
        print ("\t\tFor every number guessed right you get a cow ")
        print ("\t\tFor every number guessed right at the right place you get a bull")
        print ("\t\tYou keep guessing until you get all bulls")
        print ('\t\tNumber of digits you need to guess = %d'%len(randomNum))
        
        while bullsFound != len(randomNum) : 
                print ('\n')
                nextLetter = str(raw_input("Enter the character\t"))
                if nextLetter == 'q' : 
                        break 
                else : 
                        bullsFound = CowOrBull(randomNum, nextLetter)

        if bullsFound == len(randomNum) : 
                print ('\n\n \t\t Yaaay Found %d bulls '%bullsFound)
        else : 
                print ('QUIT QUIT QUIT')

if __name__ == '__main__' : 
        main()
