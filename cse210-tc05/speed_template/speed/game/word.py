from actor import Actor
import random
import os
class Word(Actor):
    def __init__(self):
        super(Word, self).__init__()
        os.chdir(r'speed_template/speed/game')
        file = open("words.txt")       #open file     
        dataString = file.read()  #turn file into string
        self.wordArray= dataString.split() #turn string into array
        self.value = self.wordArray[random.randint(0,len(self.wordArray)-1)]
        print(self.value)


word = Word()

