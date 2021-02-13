from game.actor import Actor
import random
import os
from pathlib import Path

"""Lives class. Used for overloading actor methods to ensure the lives display correctly
    
    Authors:
        Bethany Steiner
"""
class Lives(Actor):
    def __init__(self):
        super(Lives, self).__init__()

        self.lives = 5
        text = "Lives = "
        self.execute()

    def execute(self):
        self.set_text("Lives = "+ str(self.lives))

    def decrement_lives(self):
        self.lives -= 1