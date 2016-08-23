from __future__ import print_function
import sys
import os
import math


def main() :
        print ('This program is to learn python file operations\n')

##write to a file 
        fp = open('tmp.txt', 'w')
        fp.write('This is a file writing test \n')
        fp.write('Second line of the test\n')
        fp.write('Fill up with lines\n')
        fp.write('Make up some story\n')
        fp.close()

#read file
        fp = open('tmp.txt','r')
        print('Reading from a file\n ')
        for line in fp : 
                print (line)
        fp.close()

#reset file pointer
#        fp.seek(0)


#read file as a list of lines
        print('Reading from a file as a list of statements\n ')
        fp = open("tmp.txt","a+")
        fp.write('Rahul is practicing file operations in python')
        fp.seek(0)

        readlines = list(fp)
        for line in readlines : 
                print (line)

        fp.close()

#using 'with' keyword for file reading
        print('Using \"with\" keyword for file read \n ')
        with open('tmp.txt', 'r') as f : 
                print(f.read())

        #print('charsWriten = %d' %charsWriten)

if __name__ == '__main__' : 
        main()
