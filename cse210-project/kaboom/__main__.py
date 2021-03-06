from game.director import Director
from pathlib import Path
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.point import Point
from game.bomb import Bomb
import arcade
import random


def main():
    cast = {}
    script = {}
    arcade.open_window(600,600, "Kaboom")
   # arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
    file_dir = Path(__file__).parent
    #you have to be in the cse210-tc05 folder for the file to open

    # coordinates of image is the center of image
    texture = arcade.load_texture(file_dir/"pictures/Blue Bomb.jpg")
    scale = .4 #size\
    cast["bomb"] = [Bomb(texture,scale, Point(400,500))]

    #Create an array of the bomb pictures to be picked at random 
    texture = arcade.load_texture(file_dir/"pictures/Blue Bomb.jpg")
    ABomb = arcade.load_texture(file_dir/"pictures/Black Bomb.png")
    Bbomb = arcade.load_texture(file_dir/"pictures/Blue Bomb.jpg")
    CBomb = arcade.load_texture(file_dir/"pictures/bomb.jpg")
    DBomb = arcade.load_texture(file_dir/"pictures/RedBomb.png")
    EBomb = arcade.load_texture(file_dir/"pictures/Small B Bomb.jpg")
    bomb = ['ABomb', 'BBomb', 'CBomb', 'DBomb', 'EBomb']
    random_index = random.randrange(len(bomb))

    print(bomb[random_index])

    # arcade.draw_scaled_texture_rectangle(100, 100, texture, scale, 30)
    # arcade.finish_render()
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()

    script["update"] = [move_actors_action, handle_collisions_acition]

    director = Director(cast, script)
    print("Starting game")
    director.start_game()

main()
# program entry point