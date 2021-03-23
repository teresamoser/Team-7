import arcade
class PowerUp(arcade.Sprite):
    def __init__(self,file, scaling, type):
        super(PowerUp, self).__init__(file,scaling)
        self.type = type