import test_chess.context
from chess_classes.pieces import Piece, Pawn, Queen, King, Knight, Rook, Bishop, Super_Piece
from chess_classes.player import Player
from chess_classes.chess import ChessState
from pytest import raises


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
    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
    assert state.get_pieces_pos() == pieces_pos
    state_str = ""
    for i in range(3):
        state_str += "None, None, None, None, None, None, None, None, \n"
    state_str += "None, None, None, w_pawn is on position (3, 3), None, None, None, None, \n"
    for i in range(4):
        state_str += "None, None, None, None, None, None, None, None, \n"
    assert str(state) == state_str
