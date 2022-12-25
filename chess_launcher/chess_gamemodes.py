import context
import pygame as p
import random
from chess_classes.chess import Chess, ChessState
from chess_classes.pieces import Piece, Pawn, Queen, King, Knight, Rook, Bishop

class ClassicChess(Chess):
    def __init__(self) -> None:
        super().__init__()
        p.display.set_caption("Classic Chess")


class FischerChess(Chess):
    def __init__(self) -> None:
        super().__init__()
        p.display.set_caption("Fischer Chess")

        black_row = [None, None, None, None, None, None, None, None]
        white_row = [None, None, None, None, None, None, None, None]

        white_col = [1,3,5,7]
        black_col = [0,2,4,6]
        available_col = [0,1,2,3,4,5,6,7]

        bishop_pos_white = random.choice(white_col)
        bishop_pos_black = random.choice(black_col)
        white_row[bishop_pos_black] = Bishop('bishop', 'white', self._tile_size, (bishop_pos_black, 7))
        white_row[bishop_pos_white] = Bishop('bishop', 'white', self._tile_size, (bishop_pos_white, 7))
        black_row[bishop_pos_black] = Bishop('bishop', 'black', self._tile_size, (bishop_pos_black, 0))
        black_row[bishop_pos_white] = Bishop('bishop', 'black', self._tile_size, (bishop_pos_white, 0))
        available_col.remove(bishop_pos_black)
        available_col.remove(bishop_pos_white)

        king_pos = random.choice(available_col[1:-2])

        white_row[king_pos] = King('king', 'white', self._tile_size, (king_pos, 7))
        black_row[king_pos] = King('king', 'black', self._tile_size, (king_pos, 0))
        
        if king_pos == available_col[1]:
            available_col.remove(king_pos)
            rook_1_pos = available_col[0]
            available_col.remove(rook_1_pos)
            rook_2_pos = random.choice(available_col)
            available_col.remove(rook_2_pos)
        elif king_pos == available_col[2]:
            available_col.remove(king_pos)
            rook_1_pos = random.choice(available_col[0:2])
            available_col.remove(rook_1_pos)
            rook_2_pos = random.choice(available_col[2:])
            available_col.remove(rook_2_pos)
        elif king_pos == available_col[3]:
            available_col.remove(king_pos)
            rook_1_pos = random.choice(available_col[0:3])
            available_col.remove(rook_1_pos)
            rook_2_pos = random.choice(available_col[3:])
            available_col.remove(rook_2_pos)
        elif king_pos == available_col[4]:
            available_col.remove(king_pos)
            rook_1_pos = available_col[-1]
            available_col.remove(rook_1_pos)
            rook_2_pos = random.choice(available_col)
            available_col.remove(rook_2_pos)

        white_row[rook_1_pos] = Rook('rook', 'white', self._tile_size, (rook_1_pos, 7))
        white_row[rook_2_pos] = Rook('rook', 'white', self._tile_size, (rook_2_pos, 7))
        black_row[rook_1_pos] = Rook('rook', 'black', self._tile_size, (rook_1_pos, 0))
        black_row[rook_2_pos] = Rook('rook', 'black', self._tile_size, (rook_2_pos, 0))
        
        queen_pos = random.choice(available_col)
        available_col.remove(queen_pos)

        white_row[queen_pos] = Queen('queen', 'white', self._tile_size, (queen_pos, 7))
        black_row[queen_pos] = Queen('queen', 'black', self._tile_size, (queen_pos, 0))

        knight_1_pos = available_col[0]
        knight_2_pos = available_col[1]

        white_row[knight_1_pos] = Knight('knight', 'white', self._tile_size, (knight_1_pos, 7))
        white_row[knight_2_pos] = Knight('knight', 'white', self._tile_size, (knight_2_pos, 7))
        black_row[knight_1_pos] = Knight('knight', 'black', self._tile_size, (knight_1_pos, 0))
        black_row[knight_2_pos] = Knight('knight', 'black', self._tile_size, (knight_2_pos, 0))

        pieces_pos = [
            black_row,
            [Pawn("pawn", "black", self._tile_size, (0,1)), Pawn("pawn", "black", self._tile_size, (1,1)), 
            Pawn("pawn", "black", self._tile_size, (2,1)), Pawn("pawn", "black", self._tile_size, (3,1)), 
            Pawn("pawn", "black", self._tile_size, (4,1)), Pawn("pawn", "black", self._tile_size, (5,1)), 
            Pawn("pawn", "black", self._tile_size, (6,1)), Pawn("pawn", "black", self._tile_size, (7,1))],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn("pawn", "white", self._tile_size, (0,6)), Pawn("pawn", "white", self._tile_size, (1,6)), 
            Pawn("pawn", "white", self._tile_size, (2,6)), Pawn("pawn", "white", self._tile_size, (3,6)),
            Pawn("pawn", "white", self._tile_size, (4,6)), Pawn("pawn", "white", self._tile_size, (5,6)), 
            Pawn("pawn", "white", self._tile_size, (6,6)), Pawn("pawn", "white", self._tile_size, (7,6))],
            white_row,
        ]
        state = ChessState(self._first_player, self._second_player, self._tile_size, pieces_pos)
        self._state = state


chess = FischerChess()
chess.play()
