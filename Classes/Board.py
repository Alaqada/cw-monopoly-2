import Classes.Tile as Tile

class Board():
    def __init__(self, game):
        tiles = [0]*40
        tiles[0] = Tile.StartingTile()

        self.tiles = tiles

