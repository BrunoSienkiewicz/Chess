# https://en.wikipedia.org/wiki/Rules_of_chess
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
from pytest import raises


def test_create_piece():
    piece = Super_Piece('pawn', 'white', 100, (0,1))
    assert piece.get_type() == 'pawn'
    assert piece.get_color() == 'white'
    assert piece.get_position() == (0,1)
    assert piece.get_points() == 0


def test_create_pawn():
    piece = Pawn('pawn', 'white', 100, (0,1))
    assert piece.get_type() == 'pawn'
    assert piece.get_color() == 'white'
    assert piece.get_position() == (0,1)
    assert piece.get_points() == 1


def test_create_bishop():
    piece = Bishop('bishop', 'white', 100, (0,1))
    assert piece.get_type() == 'bishop'
    assert piece.get_color() == 'white'
    assert piece.get_position() == (0,1)
    assert piece.get_points() == 3


def test_create_knight():
    piece = Knight('knight', 'white', 100, (0,1))
    assert piece.get_type() == 'knight'
    assert piece.get_color() == 'white'
    assert piece.get_position() == (0,1)
    assert piece.get_points() == 3


def test_create_rook():
    piece = Rook('rook', 'white', 100, (0,1))
    assert piece.get_type() == 'rook'
    assert piece.get_color() == 'white'
    assert piece.get_position() == (0,1)
    assert piece.get_points() == 5


def test_create_queen():
    piece = Queen('queen', 'white', 100, (0,1))
    assert piece.get_type() == 'queen'
    assert piece.get_color() == 'white'
    assert piece.get_position() == (0,1)
    assert piece.get_points() == 9


def test_create_king():
    piece = King('king', 'white', 100, (0,1))
    assert piece.get_type() == 'king'
    assert piece.get_color() == 'white'
    assert piece.get_position() == (0,1)
    assert piece.get_points() == 0


def test_create_piece_invalid():
    with raises(TypeError):
        piece = Super_Piece('', 'white', 100, (0,1))
    with raises(TypeError):
        piece = Super_Piece('pawn', '', 100, (0,1))
    with raises(ValueError):
        piece = Super_Piece('pawn', 'white', 100, (0,-1))
    with raises(ValueError):
        piece = Super_Piece('pawn', 'white', 100, (8,8))


def test_piece_available_moves():
    piece = Super_Piece('pawn', 'white', 100, (0,1))
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
    moves_list = []
    for col in range(8):
        for row in range(8):
            moves_list.append([col, row])
    assert piece.get_moves(pieces_pos) == moves_list


def test_white_pawn_available_moves():
    piece = Pawn('pawn', 'white', 100, (3,3))
    moves_list = [(3,2),(3,1)]
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
    assert piece.get_moves(pieces_pos) == moves_list
    piece.set_position((3,2))
    moves_list = [(3,1)]
    assert piece.get_moves(pieces_pos) == moves_list


def test_black_pawn_available_moves():
    piece = Pawn('pawn', 'black', 100, (3,3))
    moves_list = [(3,4),(3,5)]
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
    assert piece.get_moves(pieces_pos) == moves_list
    piece.set_position((3,4))
    moves_list = [(3,5)]
    assert piece.get_moves(pieces_pos) == moves_list


def test_white_pawn_capture_available_moves():
    w_pawn = Pawn('pawn', 'white', 100, (3,3))
    b_pawn1 = Pawn('pawn', 'black', 100, (2,2))
    b_pawn2 = Pawn('pawn', 'black', 100, (4,2))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, b_pawn1, None, b_pawn2, None, None, None],
        [None, None, None, w_pawn, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [(3,2),(3,1),(2,2),(4,2)]
    assert w_pawn.get_moves(pieces_pos) == moves_list


def test_black_pawn_capture_available_moves():
    b_pawn = Pawn('pawn', 'black', 100, (3,3))
    w_pawn1 = Pawn('pawn', 'white', 100, (4,4))
    w_pawn2 = Pawn('pawn', 'white', 100, (2,4))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, b_pawn, None, None, None, None],
        [None, None, w_pawn2, None, w_pawn1, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [(3,4),(3,5),(2,4),(4,4)]
    assert b_pawn.get_moves(pieces_pos) == moves_list


def test_white_pawn_blocked_available_moves():
    w_pawn1 = Pawn('pawn', 'white', 100, (3,3))
    w_pawn2 = Pawn('pawn', 'white', 100, (3,2))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, w_pawn2, None, None, None, None],
        [None, None, None, w_pawn1, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = []
    assert w_pawn1.get_moves(pieces_pos) == moves_list
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, w_pawn2, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, w_pawn1, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [(3,2)]
    assert w_pawn1.get_moves(pieces_pos) == moves_list


def test_black_pawn_blocked_available_moves():
    b_pawn1 = Pawn('pawn', 'black', 100, (3,3))
    b_pawn2 = Pawn('pawn', 'black', 100, (4,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, b_pawn1, None, None, None, None],
        [None, None, None, b_pawn2, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = []
    assert b_pawn1.get_moves(pieces_pos) == moves_list
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, b_pawn1, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, b_pawn2, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [(3,4)]
    assert b_pawn1.get_moves(pieces_pos) == moves_list


def test_knight_moves():
    knight = Knight('knight', 'black', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, knight, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [(4,5),(5,4),(2,1),(1,2),(2,5),(1,4),(4,1),(5,2)]
    assert knight.get_moves(pieces_pos) == moves_list


def test_knight_blocked_moves():
    knight = Knight('knight', 'black', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, knight, None, None, None, None, None, None],
        [None, None, None, knight, None, None, None, None],
        [None, None, None, None, None, knight, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [(4,5),(2,1),(2,5),(1,4),(4,1),(5,2)]
    assert knight.get_moves(pieces_pos) == moves_list



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


def test_create_move_invalid():
    with raises(ValueError):
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
        move = ChessMove(state, piece, (8,8))
    with raises(ValueError):
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
        move = ChessMove(state, piece, (-1,7))


def test_move_piece():
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
    move = ChessMove(state, piece, (1,1))
    new_state = state.make_move(move)
    assert piece.get_position() == (1,1)
    state_str = ""
    for i in range(1):
        state_str += "None, None, None, None, None, None, None, None, \n"
    state_str += "None, w_pawn is on position (1, 1), None, None, None, None, None, None, \n"
    for i in range(6):
        state_str += "None, None, None, None, None, None, None, None, \n"
    assert str(new_state) == state_str


def test_create_players():
    player1 = Player('white', 'white')
    player2 = Player('black', 'black')
    assert player1.name() == 'white'
    assert player2.name() == 'black'
    assert player1.color() == 'white'
    assert player2.color() == 'black'
    assert player1.score() == 0
    assert player2.score() == 0


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
