from game.actor import Actor
import random
import os
from pathlib import Path
class Word(Actor):
    def __init__(self):
        super(Word, self).__init__()
        file_dir = Path(".")
        #you have to be in the cse210-tc05 folder for the file to open
        file = open(file_dir/"speed_template/speed/game/words.txt")       #open file     
        dataString = file.read()  #turn file into string
        self.wordArray= dataString.split() #turn string into array
        self.value = self.wordArray[random.randint(0,len(self.wordArray)-1)]
        self.set_text = self.value
        print(self.value)
    def get_value(self):
        return self.value

word = Word()

