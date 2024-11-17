from Tile import *
from Board import Board
from GameManager import GameManager

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.game_manager = GameManager(self)