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
        self.enemy_list = None
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
        self.enemy_list = arcade.SpriteList()

        # Set up the player
        #change player to a tray/basket
        file_dir = Path(__file__).parent.parent

        self.player_sprite = arcade.Sprite(file_dir/"pictures/bucket.png", 0.3)
        self.player_sprite.center_x = 2 * constants.GRID_PIXEL_SIZE
        self.player_sprite.center_y = 2 * constants.GRID_PIXEL_SIZE
        self.player_list.append(self.player_sprite)
        self.bomber_man_sprite = arcade.Sprite(file_dir/"pictures/bomber man.png", 0.06)
        self.bomber_man_sprite.center_x = 2 * constants.GRID_PIXEL_SIZE
        self.bomber_man_sprite.center_y = 12 * constants.GRID_PIXEL_SIZE
        self.bomber_man_sprite.change_x = 7 * constants.SPRITE_SCALING

        self.enemy_list.append(self.bomber_man_sprite)

        # Create floor
        for i in range(30):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", constants.SPRITE_SCALING)
            wall.bottom = 0
            wall.center_x = i * constants.GRID_PIXEL_SIZE
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)




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
        file_dir = Path(__file__).parent.parent
        self.enemy_list.draw()

        for x in self.moving_wall_list:
            if (x.center_y<= x.boundary_bottom + (2 * constants.GRID_PIXEL_SIZE)):
                self.moving_wall_list.remove(x)
                self.all_wall_list.remove(x)
                
                # x.set_texture(file_dir/"pictures/Explosion.png")
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

        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
    def spawn_bomb(self):
        print()
        wall = arcade.Sprite(":resources:images/tiles/bomb.png", constants.SPRITE_SCALING)
        wall.center_y = 11*constants.GRID_PIXEL_SIZE
        wall.center_x = self.bomber_man_sprite.center_x
        wall.boundary_top = 11 * constants.GRID_PIXEL_SIZE
        wall.boundary_bottom = 1 * constants.GRID_PIXEL_SIZE
        #how fast the bombs go
        wall.change_y = 7 * constants.SPRITE_SCALING
        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)
    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        # --- Manage Scrolling ---
        self.enemy_list.update()
        x = random.randint(0,70)
        if x == 4:
            self.spawn_bomb()
        # Track if we need to change the viewport
        left_boundary = self.view_left + constants.VIEWPORT_MARGIN -100
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_MARGIN + 300

  #      If the self.bomber_man_sprite hit the left boundary, reverse
        if self.bomber_man_sprite.left <= left_boundary:
            self.bomber_man_sprite.change_x *= -1
        # If the self.bomber_man_sprite hit the right boundary, reverse
        elif self.bomber_man_sprite.right > right_boundary:
            self.bomber_man_sprite.change_x *= -1
        changed = False

        # # Scroll left
        if self.player_sprite.left <= left_boundary:
            self.player_sprite.left = left_boundary
            changed = True

        # # Scroll right
        if self.player_sprite.right >= right_boundary:
            self.player_sprite.right = right_boundary
            changed = True

        # # Scroll up
        # top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.VIEWPORT_MARGIN
        # if self.player_sprite.top > top_boundary:
        #     self.view_bottom += self.player_sprite.top - top_boundary
        #     changed = True

        # # Scroll down
        # bottom_boundary = self.view_bottom + constants.VIEWPORT_MARGIN
        # if self.player_sprite.bottom < bottom_boundary:
        #     self.view_bottom -= bottom_boundary - self.player_sprite.bottom
        #     changed = True

        # If we need to scroll, go ahead and do it.
        # if changed:
        #     arcade.set_viewport(self.view_left,
        #                         constants.SCREEN_WIDTH + self.view_left,
        #                         self.view_bottom,
        #                         constants.SCREEN_HEIGHT + self.view_bottom)