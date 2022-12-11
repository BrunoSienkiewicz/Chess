# pygame documentation https://www.pygame.org/docs/
from pathlib import Path
import pygame as p
from typing import Dict, Iterable, List, Optional, Tuple
from game import Game
from move import Move
from player import Player
from state import State


class Chess(Game):
    """Class that represents chess game"""
    FIRST_PLAYER_DEFAULT_NAME = 'White'
    SECOND_PLAYER_DEFAULT_NAME = 'Black'
    PRIMARY_DEFAULT_COLOR = 'white'
    SECONDARY_DEFAULT_COLOR = 'gray'

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
        self._pices_list = ["W_pawn", "W_rook", "W_knight", "W_bishop", "W_queen", "W_king", "B_pawn", "B_rook", "B_knight", "B_bishop", "B_queen", "B_king"]

        state = ChessState(self._first_player, self._second_player)

        super().__init__(size, state)

        self._pieces_images = self._get_pieces_images()
        p.display.set_caption("Chess")
    
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
                piece = board[col][row]
                if piece != "":
                    self._draw_piece(self._pieces_images[piece], row, col)

    def _draw_piece(self, piece, row, col):
        self._window.blit(piece, p.Rect(row * self._tile_size, col * self._tile_size, self._tile_size, self._tile_size))

    def _draw_complete_board(self, state: State):
        self._draw_board()
        self._draw_pieces(state)

    def _get_pieces_images(self):
        pieces_images = {}
        for piece in self._pices_list:
            # pieces_images[piece] = p.transform.scale(p.image.load(self._project_root / f"chess/pieces/{piece}.png"), (self._tile_size, self._tile_size))
            pieces_images[piece] = p.image.load(self._project_root / f"chess/pieces/{piece}.png"), (self._tile_size, self._tile_size)
        return pieces_images

class ChessState(State):
    def __init__(self, current_player, other_player):
        self._pieces_pos = [
            ["B_rook", "B_knight", "B_bishop", "B_queen", "B_king", "B_bishop", "B_knight", "B_rook"],
            ["B_pawn", "B_pawn", "B_pawn", "B_pawn", "B_pawn", "B_pawn", "B_pawn", "B_pawn"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["W_pawn", "W_pawn", "W_pawn", "W_pawn", "W_pawn", "W_pawn", "W_pawn", "W_pawn"],
            ["W_rook", "W_knight", "W_bishop", "W_queen", "W_king", "W_bishop", "W_knight", "W_rook"],
        ]
        super().__init__(current_player, other_player)

    def get_pieces_pos(self):
        return self._pieces_pos


class ChessMove(Move):
    pass
