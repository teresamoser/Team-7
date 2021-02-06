
#will have a score and a buffer
class Score:
    """
    Lets the player know they typed the right word and updates the score.
    """
    def __init__(self):
        self.score = 0

    def _rightword(self, playerword, wordArray):

        if playerword in wordArray:
            print ('Correct!')
            self.score += len(playerword)
        else:
            print ('Incorrect.')        


        

class Player:
    """

    Stereotype:
        Structurer, Information Holder

    Attributes:
        
    """
    def __init__(self):
        """
        
        Args:
            
        """
        self.word = ''
        self.score = Score()
    
    def _addletter(self, letter):
        if not letter == '*'
            self.word += letter

    def clearword(self):
        self.word = ''

    def matchword(self, wordArray):
        self.score._rightword(self.word, wordArray)
        self.word = ''



        

        