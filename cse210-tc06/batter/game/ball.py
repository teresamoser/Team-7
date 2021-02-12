from game.actor import Actor
from game.point import Point
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
        self.starting_position = self._position

    def collide(self, collision_type):
        """collide: will change the velocity depending on what type of object the ball collides with
        collision_type: the type of object the ball collides with, such as a brick, the paddle, or a wall

        """
        if collision_type == "brick":
            self._velocity.set_y(1)
        elif collision_type == "paddle":
            self._velocity.set_y(-1)
        elif collision_type == "right_wall":
            self._velocity.set_x(-1)
        elif collision_type == "left_wall":
            self._velocity.set_x(1)
    def hit_ground(self):
        print("hit ground")
        self._position = self.starting_position
        self.random_velocity()
    def random_velocity(self):
        rand_number_x = random.randint(0,1)
        rand_number_y = random.randint(0,1)
        if rand_number_x == 0:
            rand_number_x = -1
        if rand_number_y == 0:
            rand_number_y = -1
        rand_point = Point(rand_number_x,rand_number_y)

        self.set_velocity(rand_point)
    def set_starting_position(self,position):
        self.starting_position = position  

