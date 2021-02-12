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
        score = cast["score"][0]
        score.execute()
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0]
        bricks = cast["brick"]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                ball.collide("brick")
                score.increment_score()
        if ball.get_position().get_y() == constants.MAX_Y - 1:
            if ball.get_position().get_x() >= paddle.get_position().get_x() and ball.get_position().get_x() <= paddle.get_position().get_x() + paddle.length -1:
                ball.collide("paddle")
            else:
                ball.hit_ground()
        if ball.get_position().get_x() == constants.MAX_X-1:
            ball.collide("right_wall")
        if ball.get_position().get_x() == 1:
            ball.collide("left_wall")