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

        Parameters:
            event: given pygame event
        """
        if event.type == p.MOUSEBUTTONDOWN:
            self._move_piece()
        super().make_action(event)

    def draw_current_board_state(self, state):
        """
        Draws given board state on the screen.

        Parameters:
            state: current game state
        """
        self._draw_board()
        self._draw_pieces(state)
        self._draw_score()
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

        Parameters:
            state: current game state
        """
        board = state.get_pieces_pos()
        for row in range(8):
            for col in range(8):
                piece: Piece = board[row][col]
                if piece:
                    piece.draw_piece(self._window)

    def _draw_score(self):
        """
        Draws player scores
        """

        # first player score
        player = self._first_player
        font = p.font.Font('freesansbold.ttf', self._margin//10)
        text = font.render(f'{player.name()} has {player.score()} points', True, self._secondary_color, self._primary_color)
        textRect = text.get_rect()
        textRect.center = (self._size + self._margin // 2, self._size - 50)
        self._window.blit(text, textRect)

        # second player score
        player = self._second_player
        font = p.font.Font('freesansbold.ttf', self._margin//10)
        text = font.render(f'{player.name()} has {player.score()} points', True, self._secondary_color, self._primary_color)
        textRect = text.get_rect()
        textRect.center = (self._size + self._margin // 2, 50)
        self._window.blit(text, textRect)

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
                in_check = new_state.is_in_check()
                new_state.set_in_check(in_check)

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
        """
        Initializes chess state.

        Parameters:
            current_player: player that is making a move
            other_player: player that just made a move
            tile size: size of a single tile
            pieces_pos: current pieces position on the board
        """
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
        """
        Checks if current player is in check

        Returns:
            True if player is in check
            False if player is not in check
        """
        king_pos = self.get_current_player_king_pos()
        other_player_moves = self.get_all_player_moves(self._other_player)
        if king_pos in other_player_moves:
            return True
        return False

    def get_current_player_king_pos(self):
        """
        Gets current players king position

        Returns:
            col: kings column
            row: kings row
        """
        for row in range(8):
            for col in range(8):
                piece = self._pieces_pos[row][col]
                player_color = self.get_current_player().color()
                if piece:
                    if piece.get_type() == 'king' and piece.get_color() == player_color:
                        return col, row

    def get_moves(self, col, row):
        """
        Gets piece moves

        Parameters:
            col: piece column
            row: piece row

        Returns:
            list of all available moves for given piece
        """
        piece: Piece = self._pieces_pos[row][col]
        if piece:
            return self.get_piece_legal_moves(piece)

    def get_piece_legal_moves(self, piece):
        """
        Gets piece legal moves

        Parameters:
            piece: given piece

        Returns:
            filtered piece moves
        """
        moves = piece.get_moves(self._pieces_pos)
        moves_copy = copy(moves)
        for move in moves_copy:
            if self.piece_move_results_in_check(piece, move):
                moves.remove(move)
        return moves

    def piece_move_results_in_check(self, piece, move):
        """
        Checks if given piece move results in check
        """
        simulated_pieces_pos = deepcopy(self._pieces_pos)
        simulated_piece = deepcopy(piece)
        simulated_state = ChessState(self._current_player, self._other_player, self._tile_size, simulated_pieces_pos)
        simulated_state, captured_piece = ChessMove(simulated_state, simulated_piece, move).make_move()
        if simulated_state.in_check():
            return True
        return False

    def set_pieces_pos(self, new_pieces_pos):
        self._pieces_pos = new_pieces_pos

    def make_move(self, move: Move) -> 'State':
        """
        Makes piece move

        Parameters:
            move: move to make

        Returns:
            State after the move
        """
        new_state, captured_piece = move.make_move()
        if captured_piece:
            piece_points = captured_piece.get_points()
            current_player = new_state.get_current_player()
            current_player.set_score(current_player.score()+piece_points)
        return new_state

    def get_winner(self) -> Optional[Player]:
        """
        Gets winner

        Returns:
            None if none player of the players won or is stalemate.
            Player if one of the players won
        """
        winner = None
        if self._in_check:
            king_pos = self.get_current_player_king_pos()
            moves = self.get_moves(king_pos[0], king_pos[1])
            if moves == []:
                winner = self._other_player
        return winner

    def is_finished(self) -> bool:
        """
        Checks if the game is finished
        """
        if self.get_winner():
            return True
        player_pieces = self.get_all_player_pieces(self._current_player)
        for piece in player_pieces:
            moves = self.get_piece_legal_moves(piece)
            if moves != []:
                return False
        return True

    def get_all_player_moves(self, player: Player) -> list:
        """
        Gets all of the given player pieces moves

        Parameters:
            player: Player class

        Returns:
            list of all player pieces moves
        """
        player_color = player.color()
        player_moves = []
        for row in range(8):
            for col in range(8):
                pieces_pos = self._pieces_pos
                piece = self._pieces_pos[row][col]
                if piece:
                    piece_moves = piece.get_moves(pieces_pos)
                    if piece.get_color() == player_color:
                        for move in piece_moves:
                            player_moves.append(move)
        return player_moves

    def get_all_player_pieces(self, player: Player) -> list:
        """
        Gets all of the player pieces
        """
        player_color = player.color()
        player_pieces = []
        for row in range(8):
            for col in range(8):
                pieces_pos = self._pieces_pos
                piece = self._pieces_pos[row][col]
                if piece:
                    if piece.get_color() == player_color:
                        player_pieces.append(piece)
        return player_pieces

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
        """
        Initalizes chess move

        Parameters:
            state: given game state
            piece: piece to make move with
            new_position: piece position aftet the move
        """
        self._piece = piece
        super().__init__(state, new_position)
        self._castle_move, self._dir = self._check_castle_move()

    def make_move(self) -> State:
        """
        Makes piece move

        Returns:
            state after the move and captured piece (None if none was captured)
        """
        pieces_pos = self._state.get_pieces_pos()
        starting_position = self._piece.get_position()
        col = starting_position[0]
        row = starting_position[1]
        if self._castle_move:
            rook: Rook = self._piece.get_castle_rook(pieces_pos, self._dir)
            rook_pos = rook.get_position()
            rook_col = rook_pos[0]
            rook_row = rook_pos[1]
            rook.set_position((col+self._dir, row))
            pieces_pos[row][col+self._dir] = rook
            pieces_pos[rook_row][rook_col] = None
        else:
            pieces_pos[row][col] = None
        col = self._new_position[0]
        row = self._new_position[1]
        captured_piece = pieces_pos[row][col]
        pieces_pos[row][col] = self._piece
        self._piece.set_position((col, row))
        new_pieces_pos = pieces_pos
        new_state = ChessState(self._state.get_current_player(), self._state.get_other_player(),
        self._state.get_tile_size(), new_pieces_pos)
        return new_state, captured_piece

    def _check_castle_move(self):
        """
        Checks if piece can castle

        Returns:
            True and direction of castling if can castle
            False if cannot castle
        """
        piece_type = self._piece.get_type()
        if piece_type == 'king':
            starting_position = self._piece.get_position()
            col = starting_position[0]
            diff = self._new_position[0] - col
            if abs(diff) == 2:
                return True, int(diff/abs(diff))
        return False, 1
