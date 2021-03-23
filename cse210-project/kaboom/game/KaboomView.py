from pathlib import Path
from game.point import Point
# from game.bomb import Bomb
from game import constants
import arcade
import random


class KaboomView(arcade.View):
    """ Main application class. """
    def __init__(self, level,score):
        """
        Initializer
        """

        super().__init__()

        # Sprite lists
        self.level = level
        # We use an all-wall list to check for collisions.
        self.all_wall_list = None
        self.score = score
        # Drawing non-moving walls separate from moving walls improves performance.
        self.static_wall_list = None
        self.bomb_list = None
        self.enemy_list = None
        self.player_list = None
        self.power_up_list = None

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
        self.bomb_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.power_up_list = arcade.SpriteList()

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
        self.bomb_list.draw()
        file_dir = Path(__file__).parent.parent
        self.enemy_list.draw()
        self.power_up_list.draw()

        for x in self.bomb_list:
            sound = arcade.Sound(":resources:sounds/explosion2.wav")    
            #this is in charge of deleting the bombs. The 2 * grid pixel size is the x that it disappears at.
            if (x.center_y<= x.boundary_bottom + (2 * constants.GRID_PIXEL_SIZE)):
                
                # if(bomb goes in bucket):
                #     sound = arcade.Sound(file_dir/"sounds/steam hiss.wav")

                sound.play()
                self.bomb_list.remove(x)
                
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

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.MOVEMENT_SPEED
        elif key == arcade.key.P:
            self.level_over()
    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.D or key == arcade.key.A:
            self.player_sprite.change_x = 0
    #this function spawns the bombs
    def power_up_effect(self, power_up):
        if power_up == "stretch":
            self.player_sprite._set_width(400)
        if power_up == "speed":
            self.player_sprite._set_width(400)        
    def spawn_power_up(self):
        file_dir = Path(__file__).parent.parent
        power_up = arcade.Sprite(file_dir/"pictures/strength.png", 0.2)
        power_up.center_y = 15*constants.GRID_PIXEL_SIZE
        #set the x to the enemy's location, as if he dropped it
        power_up.center_x = random.randint(1,12)*constants.GRID_PIXEL_SIZE
        power_up.boundary_top = 20 * constants.GRID_PIXEL_SIZE
        power_up.boundary_bottom = 0 
        #how fast the bombs go
        power_up.change_y = -(4 + self.level) * constants.SPRITE_SCALING
        self.power_up_list.append(power_up)
    def spawn_bomb(self):
        wall = arcade.Sprite(":resources:images/tiles/bomb.png", constants.SPRITE_SCALING)
        wall.center_y = 11*constants.GRID_PIXEL_SIZE
        #set the x to the enemy's location, as if he dropped it
        wall.center_x = self.bomber_man_sprite.center_x
        wall.boundary_top = 11 * constants.GRID_PIXEL_SIZE
        wall.boundary_bottom = 0 
        #how fast the bombs go
        wall.change_y = -(4 + self.level) * constants.SPRITE_SCALING
        self.bomb_list.append(wall)
        
    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        # --- Manage Scrolling ---
        self.enemy_list.update()
        self.power_up_list.update()
        self.bomb_list.update()
        #
        #
        #The next few lines controls how often the bombs spawn
        #
        x = random.randint(0,70-(self.level * 2))
        if x == 4:
            self.spawn_bomb()
        x = random.randint(0,400)
        if x == 4:
            self.spawn_power_up()
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

        if self.player_sprite.left <= left_boundary:
            self.player_sprite.left = left_boundary
            changed = True

        if self.player_sprite.right >= right_boundary:
            self.player_sprite.right = right_boundary
            changed = True
    def level_over(self):
        game_view = ChangeLevelView(self.level,self.score)
        self.window.show_view(game_view)        





class ChangeLevelView(arcade.View):
    def __init__(self, level,score):
        self.level = level
        self.score = score
        super().__init__()
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("You completed level " +(str)(self.level), constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Your score: " + (str)(self.score), constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")                         
        arcade.draw_text("Click to Start next level!", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2-150,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = KaboomView(self.level + 1, self.score)
        game_view.setup()
        self.window.show_view(game_view)
