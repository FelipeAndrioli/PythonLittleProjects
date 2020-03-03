#!/usr/bin/env python3

from random import randint

randomNumber = randint(1, 20)
guessNumber = 0

while (guessNumber != randomNumber):

    try:
        guessNumber = int(input("Guess the number: "))

        if (guessNumber < randomNumber):
            print("Too low")
        elif (guessNumber > randomNumber):
            print("Too high")
        else:
            print("Is not a number")

    except:
        print("The given value is not a number")

print("Nice! The number was " + str(guessNumber))
