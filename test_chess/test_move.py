import test_chess.context
from chess_classes.pieces import Pawn, Queen, King, Knight, Rook, Bishop, Super_Piece
from chess_classes.player import Player
from chess_classes.chess import ChessState, ChessMove
from pytest import raises


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
    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
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
        state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
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
        state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
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
    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
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