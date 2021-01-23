#the game class will compile all the other classes and do the rules
import random
import sys

DEFAULT_VALUE = "jumper_template\jumper\game\words.txt"
FILENAME = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_VALUE
class Game: 
    def start_game(self):
        player = Player()
        words = Words()
        theword =words.dealWord()
        display = Display( theword, player)
        keepGoing = True
        print("the Word is", theword)
        while player.lives >0 and keepGoing == True:
            guess = input("Guess a letter [a-z] or input ! to quit: ")
            while len(guess) > 1:
                print("Please only input one letter")
                guess = input("Guess a letter [a-z]: ")
            print("your input was ", guess)
            if guess == "!":
                keepGoing = False
                break
            display.display()
        

# display will handle the display part of the game
class Display:
    def __init__(self, word, player):
        self.word = word
        self.player = player
        self.length = len(word)
    def display(self):
        x = 0
        while x <self.length:
            print("_ ", end = "",flush = True)
            x +=1
        print()
        print()
        if self.player.lives > 4:
            print(" _____")
        if self.player.lives > 3:
            print("/_____\\")

        if self.player.lives > 2:
            print("\\     /")

        if self.player.lives > 1:
            print(" \\   /")
            
        if self.player.lives > 0:
            print("  \\ /")
            print("   0")
        if self.player.lives == 0:
            print("   x")
        print("  /|\\")
        print("  / \\")
        print("^^^^^^^^^^^")
            
        




    #the word class will choose the words that are needed for the jumper game
class Words:
    def __init__(self):
        file = open(FILENAME)       #open file
        dataString = file.read()  #turn file into string
        self.wordlist = dataString.split("\n")
    def dealWord(self):
        print("deal word")
        return self.wordlist[random.randint(0,len(self.wordlist)-1)]




# the player class will have the number of lives and the number of attempts the user has done
class Player:
    def __init__(self):
        self.lives = 5
        self.attempts = 0
        self.correct_counter = 0
        self.guesses = []
    def wrong_attempt(self):
        self.lives = self.lives -1
        self.attempts = self.attempts + 1
    


if __name__ == "__main__":
    game = Game()
    game.start_game()
