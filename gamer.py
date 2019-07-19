#!/usr/bin/env python
#This is a fucking game
#fucked By Saimun ahmed
import random
winning_number = random.randint(1, 100)
guess = 1
number = int(input(">> Guess a Number between 0 to 100 :: "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f" Winner.!.Winner.!.Chikken..Dinner << !! Guess Number in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("\tToo Low\t")
            guess += 1
            number = int(input(">> Guess again :: "))
        else:
            print("\tToo High\t")
            guess += 1
            number = int(input(">> Guess again ::"))

            exit(1)
