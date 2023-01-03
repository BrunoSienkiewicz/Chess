# pygame documentation https://www.pygame.org/docs/
import chess_classes.context
from pathlib import Path
import pygame as p
from typing import Dict, Iterable, List, Optional, Tuple
from copy import deepcopy, copy
from chess_classes.game import Game
from chess_classes.move import Move
from chess_classes.player import Player
from chess_classes.state import State
from chess_classes.pieces import Piece, Pawn, Queen, King, Knight, Rook, Bishop


class Chess(Game):
    """Class that represents chess game"""
    FIRST_PLAYER_DEFAULT_NAME = 'white'
    SECOND_PLAYER_DEFAULT_NAME = 'black'
    PRIMARY_DEFAULT_COLOR = 'white'
    SECONDARY_DEFAULT_COLOR = 'grey'

    def __init__(
        self, size = 800, margin=200, 
        first_player: Player = None, second_player: Player = None, 
        primary_color: p.Color = None, secondary_color: p.Color = None
    ):
        """
        Initializes game.

        Parameters:
            size: the size of the games window
            margin: size of margin where players are displayed
            first_player: the player that will go first (if None is passed, a player will be created)
            second_player: the player that will go second (if None is passed, a player will be created)
            primary_color: main color of the board (if None is passed, a color will be created)
            secondary_color: secondary color of the board (if None is passed, a color will be created)
        """
        self._first_player = first_player or Player(self.FIRST_PLAYER_DEFAULT_NAME, 'white')
        self._second_player = second_player or Player(self.SECOND_PLAYER_DEFAULT_NAME, 'black')
        self._primary_color = p.Color(primary_color or self.PRIMARY_DEFAULT_COLOR)
        self._secondary_color = p.Color(secondary_color or self.SECONDARY_DEFAULT_COLOR)
        self._move_color = p.Color('darkgray')
        self._tile_size = size//8
        default_pieces_pos = [
            [Rook("rook", "black", self._tile_size, (0,0)), Knight("knight", "black", self._tile_size, (1,0)),
            Bishop("bishop", "black", self._tile_size, (2,0)), Queen("queen", "black", self._tile_size, (3,0)), 
            King("king", "black", self._tile_size, (4,0)), Bishop("bishop", "black", self._tile_size, (5,0)), 
            Knight("knight", "black", self._tile_size, (6,0)), Rook("rook", "black", self._tile_size, (7,0))],
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
            [Rook("rook", "white", self._tile_size, (0,7)), Knight("knight", "white", self._tile_size, (1,7)), 
            Bishop("bishop", "white", self._tile_size, (2,7)), Queen("queen", "white", self._tile_size, (3,7)),
            King("king", "white", self._tile_size, (4,7)), Bishop("bishop", "white", self._tile_size, (5,7)), 
            Knight("knight", "white", self._tile_size, (6,7)), Rook("rook", "white", self._tile_size, (7,7))],
        ]

        p.display.set_caption("Chess")

        state = ChessState(self._first_player, self._second_player, self._tile_size, default_pieces_pos)

        super().__init__(size, margin, state)
    
    def make_action(self, event: p.event.Event = None):
        """
        Makes action on given event.
        """
        if event.type == p.MOUSEBUTTONDOWN:
            self._move_piece()
        super().make_action(event)

    def draw_current_board_state(self, state):
        """
        Draws given board state on the screen.
        """
        self._draw_board()
        self._draw_pieces(state)
        p.display.flip()

    # private methods

    def _draw_board(self):
        """
        Draws empty chess board on screen.
        """
        self._window.fill(self._primary_color)
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = self._primary_color
                else:
                    color = self._secondary_color
                p.draw.rect(self._window, color, (row * self._tile_size,
                col * self._tile_size, self._tile_size, self._tile_size))

    def _draw_pieces(self, state: State):
        """
        Draws pieces on the board on given positions.
        """
        board = state.get_pieces_pos()
        for row in range(8):
            for col in range(8):
                piece: Piece = board[row][col]
                if piece:
                    piece.draw_piece(self._window)

    def _move_piece(self):
        """
        Moves piece to mouse position.
        """

        # get mouse position and check for pieces on this position
        col, row = self._get_mouse_pos()
        pieces_pos = self._state.get_pieces_pos()
        piece = pieces_pos[row][col]

        # check if piece is on mouse position and belongs to current player
        if piece and piece.get_color() == self._state.get_current_player().color():
            # check for available moves
            available_moves = self._state.get_moves(col,row)
            self._draw_possible_moves(available_moves)

            # get finishing position given by player
            finishing_position = tuple(self._get_piece_finishing_location())

            # check if given finishing position is in available moves
            if finishing_position in available_moves:
                # make move
                move = ChessMove(self._state, piece, finishing_position)
                new_state = self._state.make_move(move)
                new_state.swap_players()

                # update state
                self.set_state(new_state)

    def _get_piece_finishing_location(self):
        """
        Returns:
            Players desired piece position.
        """
        while not self.is_finished():
            events = p.event.get()
            for event in events:
                if event.type == p.MOUSEBUTTONDOWN:
                    return self._get_mouse_pos()
                super().make_action(event)

    def _get_mouse_pos(self):
        """
        Returns:
            players mouse position 
        """
        location = p.mouse.get_pos()
        col = location[0]//self._tile_size
        row = location[1]//self._tile_size
        return col, row

    def _draw_possible_moves(self, available_moves):
        """
        Draws available moves of given piece on the board.
        """
        for move in available_moves:
            col = move[0]
            row = move[1]
            p.draw.circle(self._window, self._move_color, 
            (col * self._tile_size + self._tile_size/2, row * self._tile_size + self._tile_size/2),
            self._tile_size/4)
        p.display.flip()


class ChessState(State):
    def __init__(self, current_player, other_player, tile_size, pieces_pos):
        self._current_player = current_player
        self._other_player = other_player
        self._tile_size = tile_size
        self._pieces_pos = pieces_pos
        self._in_check = self.is_in_check()

    def in_check(self):
        return self._in_check

    def get_tile_size(self):
        return self._tile_size

    def get_pieces_pos(self) -> list:
        return self._pieces_pos

    def set_in_check(self, in_check):
        self._in_check = in_check

    def is_in_check(self):
        king_pos = self.get_current_player_king_pos()
        for row in range(8):
            for col in range(8):
                pieces_pos = self._pieces_pos
                piece = self._pieces_pos[row][col]
                if piece:
                    player_color = self.get_current_player().color()
                    piece_moves = piece.get_moves(pieces_pos)
                    if piece.get_color() != player_color and king_pos in piece_moves:
                        pass
                        return True
        return False

    def get_current_player_king_pos(self):
        for row in range(8):
            for col in range(8):
                piece = self._pieces_pos[row][col]
                player_color = self.get_current_player().color()
                if piece:
                    if piece.get_type() == 'king' and piece.get_color() == player_color:
                        return col, row

    def get_moves(self, col, row):
        piece: Piece = self._pieces_pos[row][col]
        if piece:
            moves = piece.get_moves(self._pieces_pos)
            moves_copy = copy(moves)
            for move in moves_copy:
                simulated_pieces_pos = deepcopy(self._pieces_pos)
                simulated_piece = deepcopy(piece)
                simulated_state = ChessState(self._current_player, self._other_player, self._tile_size, simulated_pieces_pos)
                simulated_state = ChessMove(simulated_state, simulated_piece, move).make_move()
                pass
                if simulated_state.in_check():
                    moves.remove(move)
            return moves

    def set_pieces_pos(self, new_pieces_pos):
        self._pieces_pos = new_pieces_pos

    def make_move(self, move: Move) -> 'State':
        new_state = move.make_move()
        return new_state

    def get_winner(self) -> Optional[Player]:
        winner = None
        if self._in_check:
            king_pos = self.get_current_player_king_pos()
            moves = self.get_moves(king_pos[0], king_pos[1])
            if moves == []:
                winner = self._other_player
        return winner

    def is_finished(self) -> bool:
        if self.get_winner():
            return True
        return False

    def __str__(self) -> str:
        board_str = ""
        for row in range(8):
            for col in range(8):
                board_str += f"{str(self._pieces_pos[row][col])}, "
            board_str += "\n"
        return board_str

    def __deepcopy__(self, memo):
        return ChessState(self._current_player, self._other_player, 
            self._tile_size, self._pieces_pos)


class ChessMove(Move):
    def __init__(self, state, piece, new_position):
        self._piece = piece
        super().__init__(state, new_position)

    def make_move(self) -> State:
        pieces_pos = self._state.get_pieces_pos()
        starting_position = self._piece.get_position()
        col = starting_position[0]
        row = starting_position[1]
        pieces_pos[row][col] = None
        col = self._new_position[0]
        row = self._new_position[1]
        pieces_pos[row][col] = self._piece
        self._piece.set_position((col, row))
        new_pieces_pos = pieces_pos
        new_state = ChessState(self._state.get_current_player(), self._state.get_other_player(),
        self._state.get_tile_size(), new_pieces_pos)
        return new_state
