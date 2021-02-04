
import os
class Word(object):
    def __init__(self):
       print() 
os.chdir(r'speed_template/speed/game')
file = open("words.txt")       #open file
print(file.read())        