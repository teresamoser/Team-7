from game.actor import Actor
import random
import os
from pathlib import Path

"""Player class. Used for overloading actor methods to ensure the paddle behaves correctly
    
    Authors:
        Matt Tyra

    Args:
        position (Point): The given velocity.
"""


class Player(Actor):
    def __init__(self):
        super(Player, self).__init__()

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        velocity.set_y(0)
        self._velocity = velocity

