from Board import Board
from Tile import Property, BLOCKS
from Game import Game

class Player:
    def __init__(self, game):
        self.game = game
        self.position = 0
        self.lap_count = 0
        self.properties = []
        self.card = []
        self.money = 0

    def owns_property(self, property: Property):
        return property in self.properties

    def owns_block(self, block):
        for property in BLOCKS[block]:
            if not self.owns_property(property): return False
        return True