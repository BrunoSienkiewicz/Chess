import test_chess.context
from chess_classes.pieces import Pawn, Queen, King, Knight, Rook, Bishop, Super_Piece
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
    w_knight = Knight('knight', 'white', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, knight, None, None, None, None, None, None],
        [None, None, None, knight, None, None, None, None],
        [None, w_knight, None, None, None, knight, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [(4,5),(2,1),(2,5),(1,4),(4,1),(5,2)]
    assert knight.get_moves(pieces_pos) == moves_list


def test_knight_corner_moves():
    knight = Knight('knight', 'black', 100, (0,7))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [knight, None, None, None, None, None, None, None]
    ]
    moves_list = [(1,5),(2,6)]
    assert knight.get_moves(pieces_pos) == moves_list


def test_rook_moves():
    rook = Rook('rook', 'black', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, rook, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [
                    (4,3),(5,3),(6,3),(7,3),
                    (2,3),(1,3),(0,3),
                    (3,4),(3,5),(3,6),(3,7),
                    (3,2),(3,1),(3,0),
                ]
    assert rook.get_moves(pieces_pos) == moves_list


def test_rook_blocked_moves():
    rook = Rook('rook', 'black', 100, (3,3))
    w_rook = Rook('rook', 'white', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, w_rook, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, rook, None, rook, rook, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, rook, None, None, None, None]
    ]
    moves_list = [
                    (2,3),
                    (3,4),(3,5),(3,6),
                    (3,2),(3,1),
                ]
    assert rook.get_moves(pieces_pos) == moves_list


def test_rook_corner_moves():
    rook = Rook('rook', 'black', 100, (0,7))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [rook, None, None, None, None, None, None, None]
    ]
    moves_list = [
                    (1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                    (0,6),(0,5),(0,4),(0,3),(0,2),(0,1),(0,0)
                ]
    assert rook.get_moves(pieces_pos) == moves_list


def test_bishop_moves():
    bishop = Bishop('bishop', 'black', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, bishop, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [
                    (4,4),(5,5),(6,6),(7,7),
                    (2,4),(1,5),(0,6),
                    (4,2),(5,1),(6,0),
                    (2,2),(1,1),(0,0)
                ]
    assert bishop.get_moves(pieces_pos) == moves_list


def test_bishop_blocked_moves():
    bishop = Bishop('bishop', 'black', 100, (3,3))
    w_bishop = Bishop('bishop', 'white', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, w_bishop, None, None, None, None, None, None],
        [None, None, None, None, bishop, None, None, None],
        [None, None, None, bishop, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, bishop, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [
                    (4,4),(5,5),(6,6),(7,7),
                    (2,4),
                    (2,2),(1,1)
                ]
    assert bishop.get_moves(pieces_pos) == moves_list


def test_queen_moves():
    queen = Queen('queen', 'black', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, queen, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [
                    (4,3),(5,3),(6,3),(7,3),
                    (2,3),(1,3),(0,3),
                    (3,4),(3,5),(3,6),(3,7),
                    (3,2),(3,1),(3,0),
                    (4,4),(5,5),(6,6),(7,7),
                    (2,4),(1,5),(0,6),
                    (4,2),(5,1),(6,0),
                    (2,2),(1,1),(0,0)
                ]
    assert queen.get_moves(pieces_pos) == moves_list


def test_queen_blocked_moves():
    queen = Queen('queen', 'black', 100, (3,3))
    w_queen = Queen('queen', 'white', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, w_queen, None, w_queen, None, None, None, None],
        [None, None, None, None, queen, None, None, None],
        [None, None, None, queen, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, queen, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, queen, None, None, None, None]
    ]
    moves_list = [
                    (4,3),(5,3),(6,3),(7,3),
                    (2,3),(1,3),(0,3),
                    (3,4),(3,5),(3,6),
                    (3,2),(3,1),
                    (4,4),(5,5),(6,6),(7,7),
                    (2,4),
                    (2,2),(1,1)
                ]
    assert queen.get_moves(pieces_pos) == moves_list


def test_king_moves():
    king = King('king', 'black', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, king, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [
                    (4,3),(2,3),(3,4),(3,2),
                    (4,4),(2,4),(4,2),(2,2)
                ]
    assert king.get_moves(pieces_pos) == moves_list


def test_king_blocked_moves():
    king = King('king', 'black', 100, (3,3))
    w_pawn = Pawn('pawn', 'white', 100, (3,3))
    b_pawn = Pawn('pawn', 'black', 100, (3,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, w_pawn, None, None, None, None],
        [None, None, b_pawn, king, None, None, None, None],
        [None, None, b_pawn, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [
                    (4,3),(3,4),(3,2),
                    (4,4),(4,2),(2,2)
                ]
    assert king.get_moves(pieces_pos) == moves_list


def test_king_can_castle():
    king = King('king', 'black', 100, (4,3))
    l_rook = Rook('rook', 'black', 100, (0,3))
    r_rook = Rook('rook', 'black', 100, (7,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
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
                    (2,3),(6,3)
                ]
    
    assert king.can_castle(pieces_pos,1) == True
    assert king.can_castle(pieces_pos,-1) == True
    assert king.get_moves(pieces_pos) == moves_list


def test_king_cannot_castle():
    king = King('king', 'black', 100, (4,3))
    king.set_position((3,3))
    l_rook = Rook('rook', 'black', 100, (0,3))
    r_rook = Rook('rook', 'black', 100, (7,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [l_rook, None, None, king, None, None, None, r_rook],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    moves_list = [
                    (4,3),(2,3),(3,4),(3,2),
                    (4,4),(2,4),(4,2),(2,2)
                ]
    
    assert king.can_castle(pieces_pos,1) == False
    assert king.can_castle(pieces_pos,-1) == False
    assert king.get_moves(pieces_pos) == moves_list


def test_king_can_castle_one_side():
    king = King('king', 'black', 100, (4,3))
    l_rook = Rook('rook', 'black', 100, (0,3))
    l_rook._can_castle = False
    r_rook = Rook('rook', 'black', 100, (7,3))
    pieces_pos = [
        [None, None, None, None, None, None, None, None],
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
    assert king.can_castle(pieces_pos,-1) == False
    assert king.get_moves(pieces_pos) == moves_list

