from game.KaboomView import StartView
from game import constants
import arcade

def main():
    
    """ Main method """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = StartView()
    window.show_view(start_view)
   # start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()
