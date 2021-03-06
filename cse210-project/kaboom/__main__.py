import arcade
from pathlib import Path

arcade.open_window(600,600, "Kaboom")
arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
file_dir = Path(__file__).parent
#you have to be in the cse210-tc05 folder for the file to open
# coordinates of image is the center of image
#
texture = arcade.load_texture(file_dir/"pictures/bomb.jpg")
scale = .4 #size
arcade.draw_scaled_texture_rectangle(100, 100, texture, scale, 30)
arcade.finish_render()
arcade.run()

from game.director import Director
from pathlib import Path
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.bomb import Bomb

def main():
    cast = {}
    script = {}
    arcade.open_window(600,600, "Kaboom")
   # arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
    file_dir = Path(__file__).parent
    #you have to be in the cse210-tc05 folder for the file to open
    # coordinates of image is the center of image
    #
    texture = arcade.load_texture(file_dir/"pictures/bomb.jpg")
    scale = .4 #size\
    cast["bomb"] = [Bomb(texture,scale)]

    # arcade.draw_scaled_texture_rectangle(100, 100, texture, scale, 30)
    # arcade.finish_render()
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()

    script["update"] = [move_actors_action, handle_collisions_acition]

    director = Director(cast, script)
    director.start_game()

main()
# program entry point