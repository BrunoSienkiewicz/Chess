import pygame as p
import sys
sys.path.insert(1, 'E:\pipr\projekt\Chess')
from typing import Iterable, Optional
from pieces import Piece, Pawn, Queen, King, Knight, Rook, Bishop, Super_Piece
from game import Game
from move import Move
from player import Player
from state import State
from chess import ChessState, ChessMove, Chess


def test_create_piece():
    piece = Super_Piece('pawn', 'white', 100, (0,1))
    assert piece.get_type() == 'pawn'
    assert piece.get_color() == 'white'
    assert piece.get_position() == (0,1)


def test_create_chess_state():
    piece = Super_Piece('pawn', 'white', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, piece, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    state = ChessState('white', 'black', 100, pieces_pos)
    assert state.get_pieces_pos() == pieces_pos
    state_str = ""
    for i in range(3):
        state_str += "None, None, None, None, None, None, None, None, \n"
    state_str += "None, None, None, w_pawn is on position (3, 3), None, None, None, None, \n"
    for i in range(4):
        state_str += "None, None, None, None, None, None, None, None, \n"
    assert str(state) == state_str


def test_piece_available_moves():
    piece = Super_Piece('pawn', 'white', 100, (0,1))
    moves_list = []
    for col in range(8):
        for row in range(8):
            moves_list.append([col, row])
    assert piece.get_moves() == moves_list


def test_create_move():
    piece = Super_Piece('pawn', 'white', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, piece, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    state = ChessState('white', 'black', 100, pieces_pos)
    move = ChessMove(state, piece, (4,4))
    assert move.get_new_position() == (4,4)
    assert move.get_state() == state
