from game.actor import Actor
import random
import os
from pathlib import Path

"""Ball class. Used for overloading actor methods to ensure the ball behaves correctly
    
    Authors:
        Matt Tyra
"""


class Ball(Actor):
    def __init__(self):
        super(Ball, self).__init__()

    def collide(self, collision_type):
        """collide: will change the velocity depending on what type of object the ball collides with
        collision_type: the type of object the ball collides with, such as a brick, the paddle, or a wall

        """
        if collision_type == "brick":
            print("touching brick")
            self._velocity.set_y(1)
        elif collision_type == "paddle":
            print("paddle")
            self._velocity.set_y(-1)
        elif collision_type == "right_wall":
            print("r_wall")
            self._velocity.set_x(-1)
        elif collision_type == "left_wall":
            print("l_wall")
            self._velocity.set_x(1)


