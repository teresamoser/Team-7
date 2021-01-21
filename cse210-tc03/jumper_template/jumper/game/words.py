#this class will choose the words that are needed for the jumper game

class Words:
    def __init__(self):
        words = ["test", "something", "chicken"]
    def dealWord(self):
        return self.words.random.randint(0,len(self.words)-1)
