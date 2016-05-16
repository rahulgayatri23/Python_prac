from __future__ import print_function
import random
import sys
import os

print("Hello World")

#comment
''' A test Program to learn python '''

#name = "Rahul" 
#print(name)
#
#number = 5+2
#print("number = ", number)
#
#number = 5-2
#print("number = ", number)
#
#number = 5/2
#print("number = ", number)
#
#number = 5*2
#print("number = ", number)
#
#number = 5%2
#print("number = ", number)
#
#number = 5**2
#print("number = ", number)
#
#number = 5//2
#print("number = ", number)
#
##list examples
#
#to_do_list = ['pack bags', 'rent truck']
#print('To Do List = ', to_do_list)
#
#extra_list = ['pay bills', 'distribute extras']
#
#final_list = [to_do_list, extra_list]
#print("final list = ", final_list)
#
#extra_list.append('scotch tape')
#print("final list = ", final_list)
#
#to_do_list.insert(1, 'carton boxes')
#print("final list = ", final_list)
#
#ultimate_list = to_do_list + extra_list
#print("ultimate list = ", ultimate_list)
#print(len(ultimate_list))
#print(max(ultimate_list))
#print(min(ultimate_list))
#
#
##tuple examples, we can use len, max and min functions on the tuples too..
#'''cant change values in a tuple, so convert them into list if we want to do so...'''
#tmp_tuple = (1,2,3,4)
#print ("tmp_tuple = ", tmp_tuple)
#
#tmp_list = list(tmp_tuple)
#print ("tmp_list = ", tmp_list)
#
##Dictionaries  - creates a unique identifier for each of the enteries
#super_hero = {'Batman' : 'Bruce Wayne',
#        'Superman': 'Clarke Kent',
#        'Spiderman' : 'Peter Parker',
#        'Wolverine' : 'Logan',
#        'Professor X' : 'Charles Xavier',
#        'Magneto' : 'Max Eisenhardt'}
#
#print('Super Heroes = ', super_hero)
#print('Super Heroes [Batman] = ', super_hero['Batman'])
#print('Super Heroes [Professor X] = ', super_hero.get('Professor X'))
#print('Super Heroes Keys = ', super_hero.keys())
#print('Super Heroes values = ', super_hero.values())
#
#age = 18
#gender = 'Male'
#
#
#if (age >= 18) : 
#    print('U r eligible to get vote and drive in India ')
#elif (age >= 21) : 
#    print(' U will be eligible to be married too ')
#elif ((age >= 18) and (gender == 'female') ) : 
#    print(' U will be eligible to be married too since u r a woman')
#
#for x in range(0, 10) : 
#        print(x, end="")
#
#print('\n')       
#
#for y in ultimate_list : 
#        print(y)
#
#super_number_list = [[1,2,3], [10,20,30], [100,200,300]]
#for x in range(0, 3) : 
#        for y in range(0, 3) : 
#                print('super number [ ', x,'] [ ', y , '] = ', super_number_list[x][y])
#
#i = 12 ; j = 1
#
#while(j != i) : 
#        j+=1
#print ("J = i with j and i = ", j, i)
#
#def fubar(fNum, lNum) : 
#        result = ((fNum + lNum)* 100) // 2
#        return result
#
#print('result = ', fubar(10,14))

#print(' Give a name') 
#ip_name = sys.stdin.readline()
#print('Hello ', ip_name)

#poem_string = """ 
#Do not go gentle in to that good night
#Old age should burn and rave at the close of the day 
#rage rage against the dying of light
#"""
#
#print('poem string = ', poem_string) 
#print('poem[1,4] = ', poem_string[1:4])
#print('poem[-6] = ', poem_string[-6:])
#
#print('%c is my fav letter in %s which comes at the position %d with a probability of %0.5f' %('R', 'Rahul', 1, 0.2))

#test_file = open("test.txt", "wb")
#print (test_file.mode)
#print (test_file.name)
#test_file.write(bytes("This is a FILE IO test in python\n"))
#test_file.close()
#test_file = open("test.txt", "r+")
#text_in_file= test_file.read()
#print(text_in_file)


class Vehicle :
        __Type = ""
        __Model = ""

        def __init__(self, Type, Model) : 
                self.__Type = Type
                self.__Model = Model

        def setType(self, typ) : 
                self.__Type = typ

        def getType(self) : 
                return self.__Type

        def setModel(self, Model) : 
                self.__Model = Model

        def getModel(self) : 
                return self.__Model

        def toString(self) : 
                return "The vehicle is {} of {} Model ".format(self.__Type, self.__Model)



bike = Vehicle("Pulsar", 2009)
print(bike.toString())
