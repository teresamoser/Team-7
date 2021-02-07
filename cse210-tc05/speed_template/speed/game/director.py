# Teresa Moser responsible for entry in Class Director
from time import sleep
from game import constants
from word import Word
from player import Player
from score import Score

class Director:
    """A code template for a person who directs the game. The responsibility of 
        this class of objects is to control the sequence of play.
        
     Stereotype:
        Controller
        
    Attributes:
        input_service (InputService): The input mechanism.
        output_service (OutputService): The output mechanism.
        keep_playing (boolean): Whether or not the game can continue.
    """

    def __init__(self, input_ser, output_ser):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_ser
        self._output_service = output_ser
        self._keep_playing = True
        self._player = Player()
        self._words = Word()
        # make default player, words

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
             self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)
       
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
         that means getting the words from player

        Args:
            self (Director): An instance of Director.
        """
        direction = self._input_service.get_word()
        self._words.move(direction)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
            this case, that means checking for a word and updating the points.

        Args:
             self (Director): An instance of Director.
        """
        self._wores()
        self._player()

        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are words are correct and updated the score. 

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(Score)
        self._output_service.flush_buffer()
        print()


# Rules of the speed game
# 1. The game begins with five words moving on the screen.
# 2. The player tries to type the words they see on the screen.
# 3. The player earns points for the words they type correctly.
# 4. If the player presses the enter key their buffer is cleared.
# 5. Play continues until the player presses the ESC key.
