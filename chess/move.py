class Move:
    """A base class for classes that represent moves in games"""
    def __init__(self, state , new_position):
        self._state = state
        self._new_position = new_position

    def get_state(self):
        return self._state

    def get_new_position(self):
        return self._new_position

    def set_state(self, new_state):
        self._state = new_state

    def make_move(self, new_state):
        self.set_state(new_state)
        return self._state
