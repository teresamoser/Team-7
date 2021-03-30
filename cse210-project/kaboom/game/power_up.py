import arcade
import time
import datetime

class PowerUp(arcade.Sprite):
    def __init__(self,file, scaling, type,timeLeft):
        super(PowerUp, self).__init__(file,scaling)
        self.type = type
        self.timeLeft =timeLeft
        self.active = False

    def diminish_time(self, delta_time):
        self.timeLeft =self.timeLeft- delta_time
        