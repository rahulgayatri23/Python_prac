from __future__ import print_function
import sys
import os
import math

searchNumber = int(raw_input('Give the number : '))
numbers = [2, 3, 5, 11, 19, 22, 28, 34, 50, 52]

startIndex = 0
stepN = 0
endIndex = len(numbers)
middleIndex = endIndex/2
logstepN = math.log(len(numbers), 2)

#First 2 if loops to check if the search number is lower or higher than the lowest and the highest numbers of the list. 
if searchNumber > numbers[-1] : 
        print(' The search number is greater than the largest number in the list')
        sys.exit(0)

if searchNumber < numbers[0] : 
        print(' The search number is lower than the smallest number in the list')
        sys.exit(0)



print ('step %d : startIndex = %d\t endIndex = %d\t middleIndex = %d ' %(stepN, startIndex,endIndex,middleIndex)) 

while numbers[middleIndex] != searchNumber and stepN < logstepN: 

        if numbers[middleIndex] > searchNumber :
                endIndex = middleIndex
                middleIndex = endIndex/2
        else : 
                startIndex = middleIndex
                middleIndex = (startIndex+endIndex) / 2

        stepN += 1
        print ('step %d : startIndex = %d\t endIndex = %d\t middleIndex = %d ' %(stepN, startIndex,endIndex,middleIndex))

if numbers[middleIndex] == searchNumber : 
        print('The number you are searching for is in the %d index of the list' %middleIndex)


if stepN >= logstepN : 
        print('Sorry couldnt find your number in our list.')
