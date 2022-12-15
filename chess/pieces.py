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

    def get_position(self):
        return self._position

    def get_color(self):
        return self._color

    def set_position(self, new_position):
        self._position = new_position
    
    def draw_piece(self, window):
        col = self._position[0]
        row = self._position[1]
        window.blit(self._image, p.Rect(col * self._size, row * self._size, self._size, self._size))

    def get_moves(self) -> list:
        available_moves = []
        for row in range(8):
            for col in range(8):
                if self._can_move_to_pos(col, row):
                    available_moves.append(col, row)
        return available_moves

    def is_in_game(self):
        return self._in_game

    # private methods

    def _can_move_to_pos(self, col, row) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self._name} is on position {self._position}"


class Pawn(Piece):
    def _can_move_to_pos(self, col, row) -> bool:
        return True


class Rook(Piece):
    def _can_move_to_pos(self, col, row) -> bool:
        return True


class Bishop(Piece):
    def _can_move_to_pos(self, col, row) -> bool:
        return True


class Queen(Piece):
    def _can_move_to_pos(self, col, row) -> bool:
        return True


class King(Piece):
    def _can_move_to_pos(self, col, row) -> bool:
        return True


class Knight(Piece):
    def _can_move_to_pos(self, col, row) -> bool:
        return True
