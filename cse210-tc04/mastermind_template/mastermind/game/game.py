

import random

#game class will compile all the other classes and call them appropriately
class Game:
    def __init__(self):
        print()



#player will account for a single player, their attempts, their name, etc
class Player:
    def __init__(self, name):
        self.name = name
        self.attempts = 0
        



#number class will deal a number
class Number:
    def __init__(self):
        length = 4
        value = random.randint(1000,9999) # could change numbers based on lengths

#the guessing class will prompt the both users to guess and send their guess to guessOutput
class Guessing:
    def __init__(self):
        print()

#guessoutput will get called by guessing. It will take a single player's guess and validate it
class GuessOutput:
    def __init__(self):
        print()

#display will get called by guessing and will display the appropriate responses
class Display:
    def __init__(self):
        print()


if __name__ == "__main__":
    game = Game()
    game.start_game()