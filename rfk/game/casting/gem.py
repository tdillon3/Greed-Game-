from game.casting.actor import Actor


class Gem(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.
    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._score = 0
        # self._message = ""
        
    def add_point(self):
        """Add one point.
        
        Returns:
            None
        """
        self._score += 1
    
    def lose_point(self):
        """Lose one point.
        
        Returns:
            None
        """
        self._score -= 1

    def get_score(self):
        """Return the new score.
        
        Returns:
            self._score: New score
        """

        return self._score