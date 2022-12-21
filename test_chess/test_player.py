import test_chess.context
import pygame as p
from typing import Iterable, Optional
from chess_classes.pieces import Piece, Pawn, Queen, King, Knight, Rook, Bishop, Super_Piece
from chess_classes.game import Game
from chess_classes.move import Move
from chess_classes.player import Player
from chess_classes.state import State
from chess_classes.chess import ChessState, ChessMove, Chess
from pytest import raises


def test_create_players():
    player1 = Player('white', 'white')
    player2 = Player('black', 'black')
    assert player1.name() == 'white'
    assert player2.name() == 'black'
    assert player1.color() == 'white'
    assert player2.color() == 'black'
    assert player1.score() == 0
    assert player2.score() == 0
