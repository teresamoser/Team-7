TeresaM
from game import constants
from game.point import Point

class Brick(Actor):
    """A visible, object for the ball to hit. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _tag (string): The actor's tag.
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """
    def __init__(self):
        """The class constructor."""
        self.brick = Brick
        self._description = ""
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_description(self):
        """Gets the artifact's description.
        
        Returns:
            string: The artifact's description.
        """
        return self._description 

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def set_description(self, description):
        """Updates the actor's description to the given one.
        
        Args:
            description (string): The given description.
        """
        self._description = description

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity

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
main
