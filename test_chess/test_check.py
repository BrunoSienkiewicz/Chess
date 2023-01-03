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
    b_queen = Queen('queen', 'black', 100, (3,2))
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
    w_bishop = Bishop('bishop', 'white', 100, (3,2))
    b_rook = Rook('rook', 'black', 100, (3,0))

    pieces_pos = [
        [None, None, None, b_rook, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, w_bishop, None, None, None, None],
        [None, None, None, w_king, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
    state.is_in_check()
    assert state.in_check() == False
    assert state.get_moves(3,2) == []


def test_check_blocking():
    w_king = King('king', 'white', 100, (3,3))
    w_queen = Queen('queen', 'white', 100, (5,2))
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
                    (3,2),(3,0)
                ]
    assert state.get_moves(5,2) == moves_list


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


def test_check_in_castle():
    king = King('king', 'black', 100, (4,3))
    l_rook = Rook('rook', 'black', 100, (0,3))
    r_rook = Rook('rook', 'black', 100, (7,3))
    w_rook = Rook('rook', 'white', 100, (2,0))
    pieces_pos = [
        [None, None, w_rook, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [l_rook, None, None, None, king, None, None, r_rook],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [
                    (5,3),(3,3),(4,4),(4,2),
                    (5,4),(3,4),(5,2),(3,2),
                    (6,3)
                ]
    
    assert king.can_castle(pieces_pos,1) == True
    assert king.can_castle(pieces_pos,-1) == True
    assert king.get_moves(pieces_pos) == moves_list



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
    assert state.get_moves(0,7) == []
    assert state.in_check() == True
    assert state.is_finished() == True
    assert state.get_winner() == state.get_other_player()


def test_stalemate():
    w_king = King('king', 'white', 100, (0,7))
    b_queen = Queen('queen', 'black', 100, (2,6))

    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, b_queen, None, None, None, None, None],
        [w_king, None, None, None, None, None, None, None]
    ]

    state = ChessState(Player('white', 'white'), Player('black', 'black'), 100, pieces_pos)
    state.is_in_check()
    assert state.get_moves(0,7) == []
    assert state.in_check() == False
    assert state.is_finished() == True
    assert state.get_winner() == None
