from game.director import Director
from pathlib import Path
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.point import Point
from game.bomb import Bomb
from game.input_service import InputService
from game.tray import Tray
from game import constants
import arcade
import random


# class main(arcade.Window):
#     def __init__(self):
#         super().__init__(constants.MAX_X, constants.MAX_Y, "Kaboom")
#         cast = {}
#         script = {}
#         arcade.open_window(600,600, "Kaboom")
#     # arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
#         file_dir = Path(__file__).parent
#         #you have to be in the cse210-tc05 folder for the file to open

#         # coordinates of image is the center of image
#         scale = .4 #size\

#         #Create an array of the bomb pictures to be picked at random 
#         ABomb = "pictures/Black Bomb.png"
#         Blbomb = "pictures/Blue Bomb.jpg"
#         Bbomb = "pictures/Blue Bomb.jpg"
#         CBomb = "pictures/bomb.jpg"
#         DBomb = "pictures/RedBomb.png"
#         EBomb = "pictures/Small B Bomb.jpg"
#         bomb = [ABomb, Bbomb, CBomb, DBomb, EBomb, Blbomb]
#         random_index = random.randrange(len(bomb))
#         texture = arcade.load_texture(file_dir/bomb[random_index])

#         cast["bomb"] = [Bomb(texture,scale, Point(400,500))]
#         tray_texture = arcade.load_texture(file_dir/"pictures/tray.jpg")
#         cast["tray"] = [Tray(tray_texture,scale,Point(300, 150))]
#         arcade.set_background_color(arcade.color.AMAZON)

#         #print(bomb[random_index])

#         # arcade.draw_scaled_texture_rectangle(100, 100, texture, scale, 30)
#         # arcade.finish_render()
#         move_actors_action = MoveActorsAction()
#         handle_collisions_acition = HandleCollisionsAction()
#     # input_service = InputService()

#         script["update"] = [move_actors_action, handle_collisions_acition]
#         #script["input"] = [input_service]

#         director = Director(cast, script)
#         print("Starting game")
#         director.start_game()

# main = main()
# main.run()
# # program entry point



"""
Sprite with Moving Platforms

Load a map stored in csv format, as exported by the program 'Tiled.'

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_moving_platforms
"""
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Kaboom"
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALING
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALING

# Physics
MOVEMENT_SPEED = 10 * SPRITE_SCALING
JUMP_SPEED = 28 * SPRITE_SCALING
GRAVITY = .9 * SPRITE_SCALING


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        super().__init__(width, height, title)

        # Sprite lists

        # We use an all-wall list to check for collisions.
        self.all_wall_list = None

        # Drawing non-moving walls separate from moving walls improves performance.
        self.static_wall_list = None
        self.moving_wall_list = None

        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0
        self.game_over = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_wall_list = arcade.SpriteList()
        self.static_wall_list = arcade.SpriteList()
        self.moving_wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 2 * GRID_PIXEL_SIZE
        self.player_sprite.center_y = 3 * GRID_PIXEL_SIZE
        self.player_list.append(self.player_sprite)

        # Create floor
        for i in range(30):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)
            wall.bottom = 0
            wall.center_x = i * GRID_PIXEL_SIZE
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)





#         #Create an array of the bomb pictures to be picked at random 

        # Create platform moving up and down
        bombList = []
        for x in range(2,random.randint(2,20)):
            bomb = Bomb(":resources:images/tiles/bomb.png",SPRITE_SCALING, Point(1 + random.randint(0,5),1+ random.randint(0,5)))
            bombList.append(bomb)
        print(len(bombList))
        for x in bombList:
            wall = arcade.Sprite(x.image, x.scale)
            wall.center_y = x._position.get_y() * GRID_PIXEL_SIZE
            wall.center_x = (x._position.get_x()) * GRID_PIXEL_SIZE
            wall.boundary_top = 10 * GRID_PIXEL_SIZE
            wall.boundary_bottom = 2 * GRID_PIXEL_SIZE
            wall.change_y = 7 * SPRITE_SCALING

            self.all_wall_list.append(wall)
            self.moving_wall_list.append(wall)
        

 

        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player_sprite,
                                           self.all_wall_list,
                                           gravity_constant=GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        self.game_over = False

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the sprites.
        self.static_wall_list.draw()
        self.moving_wall_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        # Adjust the text position based on the viewport so that we don't
        # scroll the text too.
        distance = self.player_sprite.right
        output = f"Distance: {distance}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20,
                         arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()