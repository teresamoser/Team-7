

import random

#game class will compile all the other classes and call them appropriately
class Game:
    def start_game(self):
        self.player1 = Player(input("Enter a name for player 1:"))
        self.player2 = Player(input("Enter a name for player 2:"))
        display = Display()
        self.number = Number()
        self.turn = 1
        self.guesser = Guessing()
        print("Number is ", game.number.value)
        display.displayGuess(1)



#player will account for a single player, their attempts, their name, etc
class Player:
    def __init__(self, name):
        self.name = name
        self.attempts = 0
        self.lastguess = "----"
        self.lastguessOutput = "****"
        



#number class will deal a number
class Number:
    def __init__(self):
        self.length = 4
        self.value = random.randint(1000,9999) # could change numbers based on lengths

#the guessing class will prompt the both users to guess and send their guess to guessOutput
class Guessing:
    def promptGuess(self):
        print()

#guessoutput will get called by guessing. It will take a single player's guess and validate it
class GuessOutput:
    def __init__(self):
        print()

#display will get called by guessing and will display the appropriate responses
class Display:
    def __init__(self):

        print("------------------")
        print("Player ", game.player1.name, "\t: ----, ****")
        print("Player ", game.player2.name, "\t: ----, ****")
        print("------------------")
    def displayGuess(self, turn):
        print("------------------")
        print("Player ", game.player1.name, ": ",game.player1.lastguess, game.player1.lastguessOutput)
        print("Player ", game.player2.name, ": ",game.player2.lastguess, game.player2.lastguessOutput)
        print("------------------")       



if __name__ == "__main__":
    game = Game()
    game.start_game()