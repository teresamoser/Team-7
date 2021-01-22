import importlib
import words
class Game:

    
    def start_game(self):
        words = Words()
        words.dealWord()

if __name__ == "__main__":
    game = Game()
    game.start_game()





    #this class will choose the words that are needed for the jumper game

class Words:
    def __init__(self):
        words = ["test", "something", "chicken"]
    def dealWord(self):
        print("deal word")
        return self.words.random.randint(0,len(self.words)-1)

