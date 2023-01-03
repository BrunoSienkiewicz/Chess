import chess_classes.context
from pathlib import Path
import pygame as p
from typing import Dict, Iterable, List, Optional, Tuple
from chess_classes.game import Game
from chess_classes.move import Move
from chess_classes.player import Player
from chess_classes.state import State


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
        self._image = p.transform.scale(p.image.load(self._project_root / f"pieces/{self._name}.png"), (size, size))
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

    def _in_bounds(self, col, row):
        if col > 7 or col < 0 or row > 7 or row <0:
            return False
        return True

    def _direction_moves(self, col, row, directions, rang, pieces_pos):
        available_moves = []
        for direction in directions:
            for i in rang:
                move_col = col+direction[0]*i
                move_row = row+direction[1]*i
                if self._in_bounds(move_col, move_row):
                    piece = pieces_pos[move_row][move_col]
                    if piece:
                        piece_color = piece.get_color()
                        if piece_color != self._color:
                            available_moves.append((move_col,move_row))
                        break
                    else:
                        available_moves.append((move_col,move_row))
        return available_moves

    def __str__(self) -> str:
        return f"{self._name} is on position {self._position}"

    def __deepcopy__(self, memo):
        return Piece(self._type, self._color, 
            self._size, self._position, self._points)

    def __copy__(self, memo):
        return Piece(self._type, self._color, 
            self._size, self._position, self._points)


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

        if self._in_bounds(row+diff, col-1):
            if pieces_pos[row+diff][col-1]:
                piece = pieces_pos[row+diff][col-1]
                if piece:
                    piece_color = piece.get_color()
                    if piece_color != self._color:
                        available_moves.append((col-1,row+diff))
        if self._in_bounds(row+diff, col+1):
            if pieces_pos[row+diff][col+1]:
                piece = pieces_pos[row+diff][col+1]
                if piece:
                    piece_color = piece.get_color()
                    if piece_color != self._color:
                        available_moves.append((col+1,row+diff))
        
        return available_moves

    def __deepcopy__(self, memo):
        return Pawn(self._type, self._color, 
            self._size, self._position, self._points)

    def __copy__(self, memo):
        return Pawn(self._type, self._color, 
            self._size, self._position, self._points)


class Rook(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 5):
        super().__init__(type, color, size, position, points)
        self._can_castle = True
    
    def get_moves(self, pieces_pos) -> list:
        col = self._position[0]
        row = self._position[1]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rang = [1,2,3,4,5,6,7]
        available_moves = self._direction_moves(col, row, directions, rang, pieces_pos)

        if self._starting_position != self._position:
            self._can_castle = False

        return available_moves

    def can_castle(self):
        return self._can_castle

    def __deepcopy__(self, memo):
        return Rook(self._type, self._color, 
            self._size, self._position, self._points)

    def __copy__(self, memo):
        return Rook(self._type, self._color, 
            self._size, self._position, self._points)


class Bishop(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 3):
        super().__init__(type, color, size, position, points)
    
    def get_moves(self, pieces_pos) -> list:
        col = self._position[0]
        row = self._position[1]
        directions = [(1,1),(-1,1),(1,-1),(-1,-1)]
        rang = [1,2,3,4,5,6,7]
        available_moves = self._direction_moves(col, row, directions, rang, pieces_pos)
        return available_moves

    def __deepcopy__(self, memo):
        return Bishop(self._type, self._color, 
            self._size, self._position, self._points)

    def __copy__(self, memo):
        return Bishop(self._type, self._color, 
            self._size, self._position, self._points)


class Queen(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 9):
        super().__init__(type, color, size, position, points)
    
    def get_moves(self, pieces_pos) -> list:
        col = self._position[0]
        row = self._position[1]
        directions = [
            (1,0),(-1,0),(0,1),(0,-1),
            (1,1),(-1,1),(1,-1),(-1,-1)
        ]
        rang = [1,2,3,4,5,6,7]
        available_moves = self._direction_moves(col, row, directions, rang, pieces_pos)
        return available_moves

    def __deepcopy__(self, memo):
        return Queen(self._type, self._color, 
            self._size, self._position, self._points)

    def __copy__(self, memo):
        return Queen(self._type, self._color, 
            self._size, self._position, self._points)


class King(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 0):
        super().__init__(type, color, size, position, points)
        self._can_castle = True

    def get_moves(self, pieces_pos) -> list:
        col = self._position[0]
        row = self._position[1]
        directions = [
            (1,0),(-1,0),(0,1),(0,-1),
            (1,1),(-1,1),(1,-1),(-1,-1)
        ]
        rang = [1]
        available_moves = self._direction_moves(col, row, directions, rang, pieces_pos)

        if self._starting_position != self._position:
            self._can_castle = False

        if self._can_castle:
            if self.can_castle(pieces_pos, -1):
                available_moves.append((col-2,row))
            if self.can_castle(pieces_pos, 1):
                available_moves.append((col+2,row))
        
        return available_moves

    def can_castle(self, pieces_pos, dir):
        row = self._position[1]
        col = self._position[0]

        for i in range(1,8):
            if col+i*dir > 7 or col+i*dir < 0:
                break
            if pieces_pos[row][col+i*dir]:
                pass
                piece: Piece = pieces_pos[row][col+i*dir]
                if piece.get_type() != 'rook':
                    break
                if piece.can_castle() == True:
                    return True

    def __deepcopy__(self, memo):
        return King(self._type, self._color, 
            self._size, self._position, self._points)

    def __copy__(self, memo):
        return King(self._type, self._color, 
            self._size, self._position, self._points)


class Knight(Piece):
    def __init__(self, type: str, color: str, size, position: tuple, points: int = 3):
        super().__init__(type, color, size, position, points)
    
    def get_moves(self, pieces_pos) -> list:
        col = self._position[0]
        row = self._position[1]
        directions = [(1,1),(-1,-1),(-1,1),(1,-1)]
        available_moves = []
        for direction in directions:
            moves = [
                (col+direction[0], row+direction[1]*2),
                (col+direction[0]*2, row+direction[1])
            ]
            for move in moves:
                move_col = move[0]
                move_row = move[1]
                if self._in_bounds(move_col, move_row):
                    piece = pieces_pos[move_row][move_col]
                    if piece:
                        piece_color = piece.get_color()
                        if piece_color != self._color:
                            available_moves.append((move_col,move_row))
                    else:
                        available_moves.append((move_col,move_row))
        return available_moves

    def __deepcopy__(self, memo):
        return Knight(self._type, self._color, 
            self._size, self._position, self._points)

    def __copy__(self, memo):
        return Knight(self._type, self._color, 
            self._size, self._position, self._points)
