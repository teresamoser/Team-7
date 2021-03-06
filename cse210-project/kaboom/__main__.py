import arcade
from pathlib import Path

arcade.open_window(600,600, "Kaboom")
arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
file_dir = Path(__file__).parent
#you have to be in the cse210-tc05 folder for the file to open
# coordinates of image is the center of image
#
texture = arcade.load_texture(file_dir/"pictures/RedBomb.png")
scale = .2 #size
arcade.draw_scaled_texture_rectangle(100, 100, texture, scale, 30)
arcade.finish_render()
arcade.run()


# program entry point