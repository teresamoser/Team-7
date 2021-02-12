#do the brick class. Right now the ball bounces off of the bricks only from below,
#  but the bricks to not disappear
from game.actor import Actor
import random
import os
from pathlib import Path

"""Brick class. Used for overloading actor methods to ensure the brick behaves correctly
    
    Authors:
       Teresa Moser
"""

class Brick(Actor):
  
    """ collision: When the ball collides with the bricks, we need the brick to disappear after collision
    """
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        bricks = cast["brick"]
        for brick in bricks:
            edge = intersect(brick, self.ball)
            if not edge:
                continue
 
            self.bricks.remove(brick)
            self.objects.remove(brick)
            self.score += self.points_per_brick

            if edge in ('top', 'bottom'):
                self.ball.velocity = (s[0], -s[1])
            else:
                self.ball.velocity = (-s[0], s[1])