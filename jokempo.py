#!/usr/bin/env python3

from random import randint

def ComputerMove():

    move = [["Paper"],
            ["Scissor"],
            ["Rock"]]

    return move[randint(0, 2)]

def GameRules(userMove, computerMove):

    #Victory = 1 - Computer Win!
    #Victory = 2 - Tie!
    #Victory = 3 - User Win!

    if (userMove == computerMove):
        return 2
    elif (userMove == 0 and computerMove == 1):
        return 1
    elif (userMove == 1 and computerMove == 0):
        return 3
    elif (userMove == 1 and computerMove == 2):
        return 1
    elif (userMove == 2 and computerMove == 1):
        return 3
    elif (userMove == 0 and computerMove == 2):
        return 3
    elif (userMove == 2 and computerMove == 0):
        return 1

def ConvertWinner(winner):
    if(winner == 1):
        return "Computer Win!"
    elif(winner == 3):
        return "User Win!"
    elif(winner == 2):
        return "Tied!"

def ValidOption(inputOption):

    if(inputOption <= 2 and inputOption > 0):
        return True
    else:
        return False

userMove = 0


try:
    userMove = int(input("Make your move: "))
except:
    print("You should make an valid move!")
