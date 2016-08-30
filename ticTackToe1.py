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
        print('\n')

def fillBoard(boardSize) : 

        firstRow = list(input('Enter the first row elements seperated by a comma : '))
        secondRow = list(input('Enter the second row elements seperated by a comma : '))
        thirdRow = list(input('Enter the third row  elements seperated by a comma : '))
        board = [firstRow, secondRow, thirdRow]

        return board

def InitStage(boardSize) : 
        firstRow = [0,0,0]
        secondRow = [0,0,0]
        thirdRow = [0,0,0]

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

        if board[0][2] != 0 :
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

        return winner

def isInBound(playerInput) : 
        if int(playerInput[0]) > 2 or int(playerInput[2]) > 2 : 
                return 0
        else : 
                return 1


def playGame(board, boardSize) : 
        index = 0
        winner = 0
        gameSts = str(raw_input('\'C\' for Continue, \'Q\' for Quit : '))

        while(gameSts != 'Q') : 
                if index%2 == 0 : 
                        playerInput = list(raw_input('Player 1 enter your input : '))
                        if isInBound(playerInput) : 
                                board[int(playerInput[0])][int(playerInput[2])] = 'X'
                                printBoard(board, boardSize)
    
                                #check if player 1 has won already
                                winner = whoIsWinner(board, boardSize)
                                if winner != 0 : 
                                        return winner
                        else : 
                                print('Player 1: Loose your chance as you are out of bounds')
                else : 
                        playerInput = list(raw_input('Player 2 enter your input : '))
                        if isInBound(playerInput) : 
                                board[int(playerInput[0])][int(playerInput[2])] = 'Y'
                                printBoard(board, boardSize)

                                #check if player 2 has won already
                                winner = whoIsWinner(board, boardSize)
                                if winner != 0 : 
                                        return winner
                        else : 
                                print('Player 2: Loose your chance as you are out of bounds')

                index+=1
                gameSts = str(raw_input('\'C\' for Continue, \'Q\' for Quit : '))
                
        return winner


def main() :
                print('********* X - represents player 1 \n *********Y-represents player 2*********')
                print('*********Alternatively player 1 and 2 will enter their input into the board*********')
                print('*********The input should be of the form \'row,column\' where the player wants to place his move in the current board*********')
                print('*********The index starts from 0, board size-1. So the left top corner index is \(0,0\) and the bottom right corner index is \(2,2\)*******' )

                boardSize = int(raw_input('Enter the size of the board  that you want : '))

        #       printBoardSkeleton(boardSize)
        #
        #        board = fillBoard(boardSize)
        #        printBoard(board, boardSize)
        #
        #        winner = whoIsWinner(board, boardSize)
        #
                print('\n\n Tic Tac Toe board of size %d\n\n'%boardSize)

                board = InitStage(boardSize)
                printBoard(board, boardSize)


                winner = playGame(board, boardSize)
                if winner != 0 : 
                        print('The Winner is ', winner)

if __name__ == '__main__' : 
        main()
