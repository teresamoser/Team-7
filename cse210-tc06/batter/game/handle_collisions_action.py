import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Authors:
        Matt Tyra
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0]
        bricks = cast["brick"]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                print("touching")
                ball.collide("brick")
        if ball.get_position().equals(paddle.get_position()):
            ball.collide("paddle")
        if ball.get_position().get_x() == constants.MAX_X-1:
            ball.collide("right_wall")
        if ball.get_position().get_x() == 1:
            ball.collide("left_wall")