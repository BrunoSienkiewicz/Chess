import pygame as p
from typing import Iterable, Optional
from pieces import Piece, Pawn, Queen, King, Knight, Rook, Bishop, Super_Piece
from game import Game
from move import Move
from player import Player
from state import State
from chess import ChessState, ChessMove, Chess


chess = Chess()
chess.play()
