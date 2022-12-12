# pygame documentation https://www.pygame.org/docs/
from pathlib import Path
import pygame as p
from typing import Dict, Iterable, List, Optional, Tuple
from game import Game
from move import Move
from player import Player
from state import State
from pieces import Piece, Pawn, Queen, King, Knight, Rook, Bishop


class Chess(Game):
    """Class that represents chess game"""
    FIRST_PLAYER_DEFAULT_NAME = 'White'
    SECOND_PLAYER_DEFAULT_NAME = 'Black'
    PRIMARY_DEFAULT_COLOR = 'white'
    SECONDARY_DEFAULT_COLOR = 'grey'

    def __init__(self, size = 800, margin=10, first_player: Player = None, second_player: Player = None, primary_color: p.Color = None, secondary_color: p.Color = None):
        """
        Initializes game.

        Parameters:
            size: the size of the games window
            first_player: the player that will go first (if None is passed, a player will be created)
            second_player: the player that will go second (if None is passed, a player will be created)
        """
        self._first_player = first_player or Player(self.FIRST_PLAYER_DEFAULT_NAME)
        self._second_player = second_player or Player(self.SECOND_PLAYER_DEFAULT_NAME)
        self._primary_color = p.Color(primary_color or self.PRIMARY_DEFAULT_COLOR)
        self._secondary_color = p.Color(secondary_color or self.SECONDARY_DEFAULT_COLOR)
        self._tile_size = size//8

        p.display.set_caption("Chess")

        state = ChessState(self._first_player, self._second_player, self._tile_size)

        super().__init__(size, state)
    
    def make_action(self, event: p.event.Event = None):
        super().make_action(event)

    def draw_current_board_state(self, state):
        self._draw_complete_board(state)

    # private methods

    def _draw_board(self):
        self._window.fill(self._primary_color)
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = self._primary_color
                else:
                    color = self._secondary_color
                p.draw.rect(self._window, color, (row * self._tile_size, col * self._tile_size, self._tile_size, self._tile_size))
        p.display.flip()

    def _draw_pieces(self, state: State):
        board = state.get_pieces_pos()
        for row in range(8):
            for col in range(8):
                piece: Piece = board[col][row]
                if piece:
                    piece.draw_piece(row, col, self._window)

    def _draw_complete_board(self, state: State):
        self._draw_board()
        self._draw_pieces(state)


class ChessState(State):
    def __init__(self, current_player, other_player, tile_size):
        self._tile_size = tile_size
        self._pieces_pos = [
            [Rook("rook", "black", self._tile_size, (0,0)), Knight("knight", "black", self._tile_size, (0,1)), Bishop("bishop", "black", self._tile_size, (0,2)), Queen("queen", "black", self._tile_size, (0,3)), 
            King("king", "black", self._tile_size, (0,4)), Bishop("bishop", "black", self._tile_size, (0,5)), Knight("knight", "black", self._tile_size, (0,6)), Rook("rook", "black", self._tile_size, (0,7))],
            [Pawn("pawn", "black", self._tile_size, (1,0)), Pawn("pawn", "black", self._tile_size, (1,1)), Pawn("pawn", "black", self._tile_size, (1,2)), Pawn("pawn", "black", self._tile_size, (1,3)), 
            Pawn("pawn", "black", self._tile_size, (1,4)), Pawn("pawn", "black", self._tile_size, (1,5)), Pawn("pawn", "black", self._tile_size, (1,6)), Pawn("pawn", "black", self._tile_size, (1,7))],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn("pawn", "white", self._tile_size, (6,0)), Pawn("pawn", "white", self._tile_size, (6,1)), Pawn("pawn", "white", self._tile_size, (6,2)), Pawn("pawn", "white", self._tile_size, (6,3)),
            Pawn("pawn", "white", self._tile_size, (6,4)), Pawn("pawn", "white", self._tile_size, (6,5)), Pawn("pawn", "white", self._tile_size, (6,6)), Pawn("pawn", "white", self._tile_size, (6,7))],
            [Rook("rook", "white", self._tile_size, (7,0)), Knight("knight", "white", self._tile_size, (7,1)), Bishop("bishop", "white", self._tile_size, (7,2)), Queen("queen", "white", self._tile_size, (7,3)),
            King("king", "white", self._tile_size, (7,4)), Bishop("bishop", "white", self._tile_size, (7,5)), Knight("knight", "white", self._tile_size, (7,6)), Rook("rook", "white", self._tile_size, (7,7))],
        ]
        # self._pieces_pos = [
        #     [Pawn("pawn", "black", self._tile_size, (1,0)), Pawn("pawn", "black", self._tile_size, (1,1)), Pawn("pawn", "black", self._tile_size, (1,2)), Pawn("pawn", "black", self._tile_size, (1,3)), 
        #     Pawn("pawn", "black", self._tile_size, (1,4)), Pawn("pawn", "black", self._tile_size, (1,5)), Pawn("pawn", "black", self._tile_size, (1,6)), Pawn("pawn", "black", self._tile_size, (1,7))],
        #     [Pawn("pawn", "black", self._tile_size, (1,0)), Pawn("pawn", "black", self._tile_size, (1,1)), Pawn("pawn", "black", self._tile_size, (1,2)), Pawn("pawn", "black", self._tile_size, (1,3)), 
        #     Pawn("pawn", "black", self._tile_size, (1,4)), Pawn("pawn", "black", self._tile_size, (1,5)), Pawn("pawn", "black", self._tile_size, (1,6)), Pawn("pawn", "black", self._tile_size, (1,7))],
        #     [None, None, None, None, None, None, None, None],
        #     [None, None, None, None, None, None, None, None],
        #     [None, None, None, None, None, None, None, None],
        #     [None, None, None, None, None, None, None, None],
        #     [Pawn("pawn", "white", self._tile_size, (6,0)), Pawn("pawn", "white", self._tile_size, (6,1)), Pawn("pawn", "white", self._tile_size, (6,2)), Pawn("pawn", "white", self._tile_size, (6,3)),
        #     Pawn("pawn", "white", self._tile_size, (6,4)), Pawn("pawn", "white", self._tile_size, (6,5)), Pawn("pawn", "white", self._tile_size, (6,6)), Pawn("pawn", "white", self._tile_size, (6,7))],
        #     [Pawn("pawn", "white", self._tile_size, (6,0)), Pawn("pawn", "white", self._tile_size, (6,1)), Pawn("pawn", "white", self._tile_size, (6,2)), Pawn("pawn", "white", self._tile_size, (6,3)),
        #     Pawn("pawn", "white", self._tile_size, (6,4)), Pawn("pawn", "white", self._tile_size, (6,5)), Pawn("pawn", "white", self._tile_size, (6,6)), Pawn("pawn", "white", self._tile_size, (6,7))],
        # ]

        super().__init__(current_player, other_player)

    def get_pieces_pos(self) -> list:
        return self._pieces_pos

    def get_moves(self, row, col):
        piece: Piece = self._pieces_pos[col][row]
        if piece:
            return piece.get_moves()

    def make_move(self, move: Move) -> 'State':
        new_state = move.move()
        return new_state


class ChessMove(Move):
    pass