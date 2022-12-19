class Player:
    """A class that represents a player in a game"""
    def __init__(self, name: str, color: str, score: int=0) -> None:
        """
        Initializes a player.

        Parameters:
            char: a single-character string to represent the player in textual representations of game state
        """
        if len(name) == 0:
            raise ValueError('Name that represents player cannot be empty')

        self._name = name
        self._color = color
        self._score = score

    def name(self):
        return self._name

    def color(self):
        return self._color

    def score(self):
        return self._score

    def set_score(self, new_score):
        self._score = new_score
