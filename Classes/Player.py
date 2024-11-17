from Classes.Tile import BLOCKS


class Player:
    def __init__(self, game):
        self.game = game
        self.position = 0
        self.lap_count = 0
        self.properties = []
        self.cards = []
        self.money = 0

    def owns_property(self, property) -> bool:
        return property in self.properties

    def owns_block(self, block) -> bool:
        for property in BLOCKS[block]:
            if not self.owns_property(property): return False
        return True