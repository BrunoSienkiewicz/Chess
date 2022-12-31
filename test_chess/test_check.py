import test_chess.context
from chess_classes.pieces import Pawn, Queen, King, Knight, Rook, Bishop, Super_Piece
from chess_classes.chess import ChessState
from chess_classes.player import Player
from pytest import raises


def test_standard_check():
    w_king = King('king', 'white', 100, (3,3))
    b_queen = Queen('queen', 'black', 100, (3,2))

    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, b_queen, None, None, None, None],
        [None, None, None, w_king, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
    state.is_in_check()
    assert state.in_check() == True

    moves_list = [
                    (3,2),
                    (4,4),(2,4)
                ]
    assert state.get_moves(3,3) == moves_list


def test_check_cannot_capture():
    w_king = King('king', 'white', 100, (3,3))
    b_queen = Queen('queen', 'black', 100, (2,3))
    b_rook = Rook('rook', 'black', 100, (3,0))

    pieces_pos = [
        [None, None, None, b_rook, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, b_queen, None, None, None, None],
        [None, None, None, w_king, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
    state.is_in_check()
    assert state.in_check() == True

    moves_list = [
                    (4,4),(2,4)
                ]
    assert state.get_moves(3,3) == moves_list


def test_pinned():
    w_king = King('king', 'white', 100, (3,3))
    w_queen = Queen('queen', 'white', 100, (2,3))
    b_rook = Rook('rook', 'black', 100, (3,0))

    pieces_pos = [
        [None, None, None, b_rook, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, w_queen, None, None, None, None],
        [None, None, None, w_king, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
    state.is_in_check()
    assert state.in_check() == False
    assert state.get_moves(3,2) == None


def test_check_blocking():
    w_king = King('king', 'white', 100, (3,3))
    w_queen = Queen('queen', 'white', 100, (2,5))
    b_rook = Rook('rook', 'black', 100, (3,0))

    pieces_pos = [
        [None, None, None, b_rook, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, w_queen, None, None],
        [None, None, None, w_king, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
    state.is_in_check()
    assert state.in_check() == True

    moves_list = [
                    (3,0),(2,3)
                ]
    assert state.get_moves(2,5) == moves_list


def test_check_in_available_moves():
    w_king = King('king', 'white', 100, (3,3))
    b_rook = Rook('rook', 'black', 100, (2,0))

    pieces_pos = [
        [None, None, b_rook, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, w_king, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
    state.is_in_check()
    assert state.in_check() == False
    moves_list = [
                    (4,3),(3,4),(3,2),
                    (4,4),(4,2),
                ]
    assert state.get_moves(3,3) == moves_list


def test_checkmate():
    w_king = King('king', 'white', 100, (0,7))
    b_rook = Rook('rook', 'black', 100, (1,0))
    b_queen = Queen('queen', 'black', 100, (1,6))

    pieces_pos = [
        [None, b_rook, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, b_queen, None, None, None, None, None, None],
        [w_king, None, None, None, None, None, None, None]
    ]
    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
    state.is_in_check()
    assert state.get_moves(0,7) == None
    assert state.in_check() == True
    assert state.is_finished() == True
    assert state.get_winner() == Player('black', 'black')
