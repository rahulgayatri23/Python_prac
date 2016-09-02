from __future__ import print_function
import sys

def checkInput(playerInput) : 
    while playerInput != 'R' and playerInput != 'S' and playerInput != 'P' : 
        print('Not the right input')
        print (' R - rock \t S - scissors \t P - Paper ')
        playerInput = str(raw_input('Enter the input again : '))

    return playerInput


def whoWins(player1, player2) : 
    if player1 == 'R' and player2 == 'S' : 
        print('Rock wins over Scissors')
        return player1
    else : 
        if player1 == 'S' and player2 == 'P' : 
            print('Scissors wins over Paper')
            return player1
        else :
            if player1 == 'P' and player2 == 'R' : 
                print('Paper wins over Rock')
                return player1

    return 0

def main() : 
    print ('Welcome to the game of rock paper scissors')
    print ('Its a 2 player game, the rules are ')
    print (' Rock beats scissors \n Scissors beats paper \n Paper beats rock')
    print (' R - rock \t S - scissors \t P - Paper ')

    player1Input = str(raw_input('Player 1 Enter your play : '))
    player1Input = checkInput(player1Input)
    
    player2Input = str(raw_input('Player 2 Enter your play : '))
    player2Input = checkInput(player2Input)

    if  whoWins(player1Input, player2Input) : 
        print ('And the winner is player 1 ' ) 
    else :
        winner = whoWins(player2Input, player1Input)
        print ('And the winner is player 2 ') 

if __name__ == '__main__' : 
    main()
