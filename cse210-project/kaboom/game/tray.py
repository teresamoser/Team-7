from game.actor import Actor
from game import constants

class Tray(Actor):
    def __init__(self, position):
        self.set_position(position)


    def move_tray(self, mouse_x):
        point = self.get_position()
        x = point.get_x()
        x = x + mouse_x
        if x < 0:
            x = 0
        elif x > constants.MAX_X:
            x = constants.MAX_X
        point.set_x(x)
        self.set_position(point)