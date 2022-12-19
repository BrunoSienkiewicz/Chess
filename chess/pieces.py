from pathlib import Path
import pygame as p
from typing import Dict, Iterable, List, Optional, Tuple
from game import Game
from move import Move
from player import Player
from state import State


class Piece():
    def __init__(self, type: str, color: str, size, position: tuple, points: int=0):
        self._project_root = Path(__file__).parent.parent
        if type == "":
            raise TypeError('Piece must have type')
        self._type = type
        if color == "":
            raise TypeError('Piece must have assigned color')
        self._color = color
        if position[0] > 7 or position[0] < 0 or position[1] > 7 or position[1] < 0:
            raise ValueError('Invalid starting position')
        self._position = position
        self._starting_position = position
        self._name = f"{color[0]}_{type}"
        self._image = p.transform.scale(p.image.load(self._project_root / f"chess/pieces/{self._name}.png"), (size, size))
        self._size = size
        self._in_game = True
        self._points = points

    def get_type(self):
        return self._type

    def get_position(self):
        return self._position

    def get_color(self):
        return self._color

    def get_points(self):
        return self._points

    def get_starting_position(self):
        return self._starting_position

    def set_position(self, new_position):
        self._position = new_position
    
    def draw_piece(self, window):
        col = self._position[0]
        row = self._position[1]
        window.blit(self._image, p.Rect(col * self._size, row * self._size, self._size, self._size))

    def get_moves(self, pieces_pos) -> list:
        available_moves = []
        for col in range(8):
            for row in range(8):
                available_moves.append([col, row])
        return available_moves

    def is_in_game(self):
        return self._in_game

    # private methods

    def __str__(self) -> str:
        return f"{self._name} is on position {self._position}"


class Super_Piece(Piece):
    pass


class Pawn(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 1):
        super().__init__(type, color, size, position, points)

    def get_moves(self, pieces_pos) -> list:
        col = self._position[0]
        row = self._position[1]
        diff = -1 if self._color == 'white' else 1
        available_moves = []

        if self._position == self._starting_position:
            # starting position moves
            for i in range(1,3):
                if pieces_pos[row+diff*i][col]:
                    break
                available_moves.append((col,row+diff*i))
        else:
            # standard move
            if not pieces_pos[row+diff][col]:
                available_moves.append((col,row+diff))

        # capturing moves
        if pieces_pos[row+diff][col-1]:
            piece = pieces_pos[row+diff][col-1]
            if piece.get_color() != self._color:
                available_moves.append((col-1,row+diff))
        if pieces_pos[row+diff][col+1]:
            piece = pieces_pos[row+diff][col+1]
            if piece.get_color() != self._color:
                available_moves.append((col+1,row+diff))
        
        return available_moves


class Rook(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 5):
        super().__init__(type, color, size, position, points)
    
    def get_moves(self, pieces_pos) -> list:
        return True


class Bishop(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 3):
        super().__init__(type, color, size, position, points)
    
    def get_moves(self, pieces_pos) -> list:
        return True


class Queen(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 9):
        super().__init__(type, color, size, position, points)
    
    def get_moves(self, pieces_pos) -> list:
        return True


class King(Piece):
    def get_moves(self, pieces_pos) -> list:
        return True


class Knight(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 3):
        super().__init__(type, color, size, position, points)
    
    def get_moves(self, pieces_pos) -> list:
        col = self._position[0]
        row = self._position[1]
        directions = [(1,1),(-1,-1),(-1,1),(1,-1)]
        available_moves = []
        for direction in directions:
            move_col = col+direction[0]
            move_row = row+direction[1]*2
            if not pieces_pos[move_row][move_col]:
                available_moves.append((move_col,move_row))
            move_col = col+direction[0]*2
            move_row = row+direction[1]
            if not pieces_pos[move_row][move_col]:
                available_moves.append((move_col,move_row))
        return available_moves
