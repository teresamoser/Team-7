from game.actor import Actor
import random
import os
from pathlib import Path

"""Score class. Used for overloading actor methods to ensure the score displays correctly
    
    Authors:
        Matt Tyra
"""


class Score(Actor):
    def __init__(self):
        super(Score, self).__init__()

        self.score = 0
        text = "Score = "
        self.set_text(text)

    def execute(self):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self.set_text("Score = "+ str(self.score))
    def increment_score(self):
        self.score += 1
