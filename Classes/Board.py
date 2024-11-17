import Tile
from Game import Game

class Board():
    def __init__(self, game: Game):
        tiles = [0]*40
        tiles[0] = Tile.StartingTile()

        self.tiles = tiles

