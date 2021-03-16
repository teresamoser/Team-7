from pathlib import Path
from game.point import Point
from game.bomb import Bomb
from game import constants
import arcade
import random


class KaboomView(arcade.View):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """

        super().__init__()

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
        #change player to a tray/basket
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", constants.SPRITE_SCALING)
        self.player_sprite.center_x = 2 * constants.GRID_PIXEL_SIZE
        self.player_sprite.center_y = 3 * constants.GRID_PIXEL_SIZE
        self.player_list.append(self.player_sprite)

        # Create floor
        for i in range(30):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", constants.SPRITE_SCALING)
            wall.bottom = 0
            wall.center_x = i * constants.GRID_PIXEL_SIZE
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)





        #maybe have an enemy that has a bomb list, the enemy then randomly adds bombs to their bag and thus the screen overtime
        # Create platform moving up and down
        bombList = []
        for x in range(2,random.randint(2,20)):
            bomb = Bomb(":resources:images/tiles/bomb.png",constants.SPRITE_SCALING, Point(1 + random.randint(0,5),1+ random.randint(0,5)))
            bombList.append(bomb)
        print(len(bombList))
        for x in bombList:
            wall = arcade.Sprite(x.image, x.scale)
            wall.center_y = x._position.get_y() * constants.GRID_PIXEL_SIZE
            wall.center_x = (x._position.get_x()) * constants.GRID_PIXEL_SIZE
            wall.boundary_top = 10 * constants.GRID_PIXEL_SIZE
            
            if wall.boundary_bottom == 0 * constants.GRID_PIXEL_SIZE:
                bomb = Bomb(":resources:images/titles/explode.png", constants.SPRITE_SCALING)

            wall.change_y = 7 * constants.SPRITE_SCALING

            self.all_wall_list.append(wall)
            self.moving_wall_list.append(wall)
        

 

        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player_sprite,
                                           self.all_wall_list,
                                           gravity_constant=constants.GRAVITY)

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
                self.player_sprite.change_y = constants.JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = constants.MOVEMENT_SPEED

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
        left_boundary = self.view_left + constants.VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + constants.VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)