import arcade
import time
import datetime

class PowerUp(arcade.Sprite):
    """
    The powerup class is a powerup of a certain type. It has a certain amount of time before it expires.
    """
    def __init__(self,file, scaling, type,timeLeft):
        super(PowerUp, self).__init__(file,scaling)
        self.type = type
        self.timeLeft =timeLeft
        self.active = False

    def diminish_time(self, delta_time):
        """
        Decreases time by delta_time.
        """
        self.timeLeft =self.timeLeft- delta_time
        