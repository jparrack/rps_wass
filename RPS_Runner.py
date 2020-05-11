#   import statements
from RPS_singleplayer import *
from RPS_multiplayer import *

#   main methods


def main_runner():
    exitCalled = False

    print("Welcome to Rock Paper Scissors")
    print("This is: Main Menu\n1. Single player\n2. Multiplayer\n3. Exit")
    grabUserInput = int(input("Enter an option: "))

    while exitCalled !=True:
        if grabUserInput == 1:
            print("Taking you to singleplayer mode... please wait")
            singleplayer()
        if grabUserInput == 2:
            print("Taking you to multiplayer mode... please wait")
            multiplayer()
        elif grabUserInput == 3:
            print("Thanks for playing")
            exitCalled = True
            exit()
        else:
            print("Invalid input. Try again")
            grabUserInput = int(input("Enter an option: "))


main_runner()
