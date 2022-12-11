class Player:
    """A class that represents a player in a game"""
    def __init__(self, name: str) -> None:
        """
        Initializes a player.

        Parameters:
            char: a single-character string to represent the player in textual representations of game state
        """
        if len(name) == 0:
            raise ValueError('Name that represents player cannot be empty')

        self._name = name

    def name(self):
        return self._name
