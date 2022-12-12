from pathlib import Path
import pygame as p
from typing import Dict, Iterable, List, Optional, Tuple
from game import Game
from move import Move
from player import Player
from state import State


class Piece():
    def __init__(self, type: str, color: str, size, position: tuple):
        self._project_root = Path(__file__).parent.parent
        self._type = type
        self._color = color
        self._position = position
        self._name = f"{color[0]}_{type}"
        self._image = p.transform.scale(p.image.load(self._project_root / f"chess/pieces/{self._name}.png"), (size, size))
        self._size = size
        self._in_game = True
    
    def draw_piece(self, row, col, window):
        window.blit(self._image, p.Rect(row * self._size, col * self._size, self._size, self._size))

    def get_moves(self, state: State) -> list:
        available_moves = []
        for row in range(8):
            for col in range(8):
                if self._can_move_to_pos(row, col):
                    available_moves.append(row, col)
        return available_moves

    def is_in_game(self):
        return self._in_game

    # private methods

    def _can_move_to_pos(self, row, col) -> bool:
        raise NotImplementedError


class Pawn(Piece):
    def _can_move_to_pos(self, row, col) -> bool:
        return True


class Rook(Piece):
    def _can_move_to_pos(self, row, col) -> bool:
        return True


class Bishop(Piece):
    def _can_move_to_pos(self, row, col) -> bool:
        return True


class Queen(Piece):
    def _can_move_to_pos(self, row, col) -> bool:
        return True


class King(Piece):
    def _can_move_to_pos(self, row, col) -> bool:
        return True


class Knight(Piece):
    def _can_move_to_pos(self, row, col) -> bool:
        return True
