

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
        # """A person taking part in a game. The responsibility of 
        #    Player is to keep track of their identity and last guess.   
        # Stereotype: 
        #      Information Holder
        #  Attributes:
        #      _name (string): The player's name.
        #      _attempts (attempts): The player's last guess.
        # """
    def __init__(self, name):
        self._name = name
        self._attempts = 0
        
        self.lastguess = "----"
        self.lastguessOutput = "****"
        
        # """The class constructor.
        # Args:
        #     self (Player): an instance of Player.
        # """
    def get_name(self):
        return self._name
    
        # """Returns the player's name.
        # Args:
        #     self (Player): an instance of Player.
        # """    
    def set_attempts(self, attempts):
        self._attempts = attempts
        
        # """Sets the player's last move to the given instance 
        #     of Move.
        # Args:
        #     self (Player): an instance of Player.
        #     move (Move): an instance of Move
        # """
        
#roster class will help keep track of multiple players.
class Roster:
        #  """A collection of players. The responsibility of Roster is to keep track of the players.
        #  Stereotype: 
        #       Information Holder
        #  Attributes:
        #    _current (integer): The index of the current player.
        #    _players (list): A list of Player objects.
        #  """
    def __init__(self):
        self.current = -1
        self.players = []
        # """The class constructor.
        # Args:
        #     self (Roster): an instance of Roster.
        # """      
    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
        # """Adds the given player to the roster
        # Args:
        #     self (Roster): An instance of Roster.
        #     player (Player): The player object to add.
        # """
    def get_current(self):
        return self.players[self.current]
        # """Gets the current player object.
        # Args:
        #     self (Roster): An instance of Roster.
        # Returns:
        #     Player: The current player.
        # """
    def next_player(self):
        self.current = (self.current + 1) % len(self.players)
        # """Advances the turn to the next player.
        # Args:
        #     self (Roster): An instance of Roster.
        # """
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
    
# Overview
# Mastermind is a game in which each player seeks to guess the secret code they've been assigned before the other players do.

# Rules
# Mastermind is played according to the following rules:
# 1. The code is a randomly generated, four digit number between 1000 and 9999.
# 2. The players take turns registering themselves by entering their name.
# 3. The players take turns guessing the secret code based on the hint that is offered. 
#    An x means a correct number in a correct position. An o means a correct number in an incorrect position. 
#    An * means an incorrect number (see interface section).
# 4. If the guess is correct, the current player wins and the game is over.
# 5. If the guess is incorrect, a new hint is generated and play continues.

# Interface:
# Enter a name for player 1: Matt
# Enter a name for player 2: John

# --------------------
# Player Matt: ----, ****
# Player John: ----, ****
# --------------------
# Matt's turn:
# What is your guess? 1111

# --------------------
# Player Matt: 1111, xooo
# Player John: ----, ****
# --------------------
# John's turn:
# What is your guess? 4356

# --------------------
# Player Matt: 1111, xooo
# Player John: 4356, oo**
# --------------------
# Matt's turn:
# What is your guess? 1234

# Matt won!
# > _

# Requirements:
# Your program must also meet the following requirements:
# 1. The program must use the Mastermind template. DONE
# 2. The program must have a README file with assignment and author names. DONE
# 3. The program must have at least six classes. DONE
# 4. Each module, class and method must have a corresponding comment using the style demonstrated in the solo checkpoint.
# 5. The game must remain generally true to the order of play described in the rules.

# Suggestions:
# Make the game your own by enhancing it any way you like. A few ideas are as follows.
# 1. Enhanced codes (longer or letters and numbers)
# 2. Enhanced input validation with user-friendly messages.
# 3. Enhanced game play (more players, limited guesses, etc).
# 4. Enhanced board representation (better ascii art)
