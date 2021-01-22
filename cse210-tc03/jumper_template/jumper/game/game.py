#the game class will compile all the other classes and display the final game
class Game:

    
    def start_game(self):
        words = Words()
        words.dealWord()

if __name__ == "__main__":
    game = Game()
    game.start_game()





    #the word class will choose the words that are needed for the jumper game

class Words:
    def __init__(self):
        words = ["test", "something", "chicken"]
    def dealWord(self):
        print("deal word")
        return self.words.random.randint(0,len(self.words)-1)




# the player class will have the number of lives and the number of attempts the user has done
class Player:
    def __init__(self):
        lives = 5
        attempts = 0
    def wrong_attempt(self):
        self.lives = self.lives -1
        self.attempts = self.attemps + 1



