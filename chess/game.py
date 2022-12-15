from pathlib import Path
import pygame as p
import sys
from typing import Iterable, Optional
from move import Move
from player import Player
from state import State


class Game:
    """Game interface."""
    def __init__(self, size, state: State):
        """
        Initializes game.

        Parameters:
            state: initial game state
        """
        self._state = state
        self._size = size
        self._window = self._get_window(size)
        self._done = False
        p.init()

    def play(self):
        """
        Launches game.
        """
        while not self._done:
            events = p.event.get()
            for event in events:
                self.make_action(event)
                self.draw_current_board_state(self._state)
            p.display.flip()

    def draw_current_board_state(self, state):
        """
        Draws current state of the game.
        """
        raise NotImplementedError

    def make_action(self, event: p.event.Event=None):
        """
        Executes action on passed event.

        Returns:
            None if no event is passed
        """
        if event == None:
            return None
        elif event.type == p.QUIT:
            self._done = True
            sys.exit()
            

    def get_moves(self) -> Iterable[Move]:
        """
        Returns:
            Possible moves
        """
        return self._state.get_moves()

    def get_current_player(self) -> Player:
        """
        Returns:
            Current player
        """
        return self._state.get_current_player()

    def make_move(self, move: Move):
        """
        Makes move.

        Parameters:
            move: move to make
        """
        self._state = self._state.make_move(move)

    def is_finished(self) -> bool:
        """
        Returns:
            If the game is finished
        """
        return self._state.is_finished()

    def get_winner(self) -> Optional[Player]:
        """
        Returns:
            Player that is the winner or None if not finished or draw
        """
        return self._state.get_winner()

    def get_players(self) -> Iterable[Player]:
        """
        Returns:
            List of players
        """
        return self._state.get_players()

    def get_state(self) -> State:
        """
        Returns:
            Current game state
        """
        return self._state

    def set_state(self, new_state: State):
        self._state = new_state

    def __str__(self) -> str:
        """
        Returns:
            Printable text represenation of the game's state
        """
        return str(self._state)

    #private methods

    def _get_window(self, size):
        """
        Returns:
            Window of given size
        """
        return p.display.set_mode((size, size))
