import context
import pygame as p
from typing import Iterable, Optional
from chess_classes.pieces import Piece, Pawn, Queen, King, Knight, Rook, Bishop, Super_Piece
from chess_classes.game import Game
from chess_classes.move import Move
from chess_classes.player import Player
from chess_classes.state import State
from chess_classes.chess import ChessState, ChessMove, Chess


chess = Chess()
chess.play()
