from game.actor import Actor
from game.point import Point
import random
import os
from pathlib import Path

class Bomb(Actor):
    def __init__(self):
        super(Bomb, self).__init__()
        # self.image = defualt image
    def __init__(self, image,scale):
        super(Bomb, self).__init__()
        self._position = Point(200,500)
        self.image = image
        self.scale = scale