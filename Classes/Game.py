from Classes.Board import Board
from Classes.GameManager import GameManager

class Game:
    def __init__(self):
        self.board = Board(self)
        self.players = []
        self.game_manager = GameManager(self)