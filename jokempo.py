#!/usr/bin/env python3

from random import randint

def ComputerMove():

#    move = [[1, "Paper"],
#            [2, "Scissor"],
#            [3. "Rock"]]

    return randint(1, 3)

def GameRules(userMove, computerMove):

    #Victory = 1 - Computer Win!
    #Victory = 3 - User Win!

    if (userMove == computerMove):
        return 2
    elif (userMove == 1 and computerMove == 3):
        return 1
    elif (userMove == 2 and computerMove == 1):
        return 3
    elif (userMove == 2 and computerMove == 3):
        return 1
    elif (userMove == 3 and computerMove == 2):
        return 3
    elif (userMove == 1 and computerMove == 3):
        return 3
    elif (userMove == 3 and computerMove == 1):
        return 1

def ConvertWinner(winner):
    if(winner == 1):
        return "Computer Win!"
    elif(winner == 3):
        return "User Win!"
    elif(winner == 2):
        return "Tied!"

def ValidOption(inputOption):

    if(inputOption <= 3 and inputOption > 0):
        return True
    else:
        return False

def ReturnMove(action):

    move = [[""],
            ["Paper"],
            ["Scissor"],
            ["Rock"]]

    return move[action]

def main():

    userMove = 0
    computerMove = ComputerMove()


    while(ValidOption(userMove) == False):
        print("1 - Paper")
        print("2 - Scissor")
        print("3 - Rock")
        print("JO")
        print("KEM")
        print("PO!")
    
        try:
            userMove = int(input("Make your move: "))
        except:
            print("You should make an valid move!")

    print("Computer action: " + str(ReturnMove(computerMove)))
    print("Your action: " + str(ReturnMove(userMove)))
    print(ConvertWinner(GameRules(userMove, computerMove)))


if __name__ == "__main__":
    main()








