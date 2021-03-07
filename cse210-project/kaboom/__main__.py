from game.director import Director
from pathlib import Path
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.point import Point
from game.bomb import Bomb
from game.input_service import InputService
from game.tray import Tray
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
    scale = .4 #size\

    #Create an array of the bomb pictures to be picked at random 
    ABomb = "pictures/Black Bomb.png"
    Blbomb = "pictures/Blue Bomb.jpg"
    Bbomb = "pictures/Blue Bomb.jpg"
    CBomb = "pictures/bomb.jpg"
    DBomb = "pictures/RedBomb.png"
    EBomb = "pictures/Small B Bomb.jpg"
    bomb = [ABomb, Bbomb, CBomb, DBomb, EBomb, Blbomb]
    random_index = random.randrange(len(bomb))
    texture = arcade.load_texture(file_dir/bomb[random_index])

    cast["bomb"] = [Bomb(texture,scale, Point(400,500))]
    cast["tray"] = [Tray(Point(300, 150))]

    #print(bomb[random_index])

    # arcade.draw_scaled_texture_rectangle(100, 100, texture, scale, 30)
    # arcade.finish_render()
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()
    input_service = InputService()

    script["update"] = [move_actors_action, handle_collisions_acition]
    script["input"] = [input_service]

    director = Director(cast, script)
    print("Starting game")
    director.start_game()

main()
# program entry point