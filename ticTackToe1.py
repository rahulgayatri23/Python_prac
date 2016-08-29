from __future__ import print_function
import random
import sys
import os
from datetime import date

def print_hzline(boardSize) : 
        print(' --- '*boardSize) 

def print_vrline(boardSize) : 
        print('|    '*(boardSize+1)) 

def printBoardSkeleton(boardSize) : 
        for index in range(0,boardSize) : 
                print_hzline(boardSize)
                print_vrline(boardSize)
        print_hzline(boardSize)

def fillBoard(boardSize) : 

        firstRow = list(input('Enter the first row elements seperated by a comma : '))
        secondRow = list(input('Enter the second row elements seperated by a comma : '))
        thirdRow = list(input('Enter the third row  elements seperated by a comma : '))
        board = [firstRow, secondRow, thirdRow]

        return board

def printBoard(board,boardSize) : 
        print('The Tick Tac Toe board is : \n')

        for i in range(0,boardSize) : 
                for j in range(0,boardSize) : 
                        print(board[i][j],end='')
                        print('\t', end='')
                print('\n')


def diagonalMatch(board) : 
        if board[0][0] != 0 : 
                if board[0][0] == board[1][1] == board[2][2] : 
                        return board[1][1]
        else : 
                if board[0][2] == board[1][1] == board[2][0] : 
                        return board[0][2]

        return 0

def rowMatch(board) : 
        if board[0][0] != 0 : 
                if board[0][0] == board[0][1] == board[0][2] : 
                        return board[0][0]

        if board[1][0] != 0 : 
                if board[1][0] == board[1][1] == board[1][2] : 
                        return board[1][2]

        if board[2][2] != 0 : 
                if board[2][0] == board[2][1] == board[2][2] : 
                        return board[2][2]


        return 0



def colMatch(board) : 
        if board[0][0] != 0 : 
                if board[0][0] == board[1][0] == board[2][0] : 
                        return board[0][0]

        if board[1][1] != 0 : 
                if board[1][1] == board[1][1] == board[1][2] : 
                        return board[0][1]

        if board[2][2] != 0 : 
                if board[2][0] == board[2][1] == board[2][2] : 
                        return board[2][2]


        return 0



def whoIsWinner(board, boardSize) : 
        
        winner = 0

        winner = diagonalMatch(board)
        if winner != 0 : 
                return winner

        winner = colMatch(board)
        if winner != 0 : 
                return winner

        winner = rowMatch(board)
        if winner != 0 : 
                return winner

def main() :

        boardSize = int(raw_input('Enter the size of the board  that you want : '))
        print('\n\n Tic Tac Toe board of size %d\n\n'%boardSize)
        #printBoardSkeleton(boardSize)

        board = fillBoard(boardSize)
        printBoard(board, boardSize)

        winner = whoIsWinner(board, boardSize)

        if winner != 0 : 
                print('The Winner is ', winner)

if __name__ == '__main__' : 
        main()
