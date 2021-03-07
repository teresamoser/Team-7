import arcade
from game.tray import Tray

class InputService(arcade.Window):
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, width, height, title):
        """The class constructor."""
        super().__init__(width, height, title)
        
       
    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = (dx - x) * -1

    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if isinstance(actor, Tray):
                    actor.move_tray(self.mouse_x)
    