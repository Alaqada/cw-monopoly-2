from Player import Player
from Tile import Property, Terrain, BLOCKS

class GameManager:
    def __init__(self, board = None):
        self.board = board
    
    ######################################
    #### methodes concernant l'argent ####
    ######################################

    @classmethod
    def add_money(cls, player: Player, amount: int):
        player.money += amount

    @classmethod
    def remove_money(cls, player: Player, amount: int):
        player.money -= amount

    ############################################
    #### methodes concernant les proprietes ####
    ############################################

    @classmethod
    def get_density(cls, terrains: list[Terrain]):
        return max(terrain.houses_count for terrain in terrains)
    
    @classmethod
    def add_property(cls, player: Player, property: Property):
        player.properties.append(property)

    @classmethod
    def remove_property(cls, player: Player, property: Property):
        player.properties.remove(property)
    
    @classmethod
    def buy_property(cls, player: Player, property: Property):
        if property.owner == None and player.money >= property.price:
            cls.add_property(player, property)
            cls.remove_money(player, property.price)

    @classmethod
    def sell_property(cls, player: Player, property: Property):
        cls.add_money(player, int(0.8*property.price))
        cls.remove_property(player, property)

    @classmethod
    def buy_house(cls, player: Player, terrain: Terrain):
        if not player.owns_block(terrain.block): return
        block_density = cls.get_density(BLOCKS[terrain.block])
        if terrain.houses_count == block_density:
            for t in BLOCKS[terrain.block]:
                if t.houses_count < block_density: return
        if player.money >= terrain.per_house_price:
            cls.remove_money(player, terrain.per_house_price)
            terrain.build_house()

    @classmethod
    def sell_house(cls, player: Player, terrain : Terrain):
        if not player.owns_property(terrain) or terrain.houses_count == 0: return
        block_density = cls.get_density(BLOCKS[terrain.block])
        if terrain.houses_count < block_density: return
        terrain.destroy_house()

    ##############################################
    #### methodes concernant les deplacements ####
    ##############################################

    @classmethod
    def move_player(cls, player: Player, displacement: int):
        player.position = (player.position + displacement) % 40
        player.lap_count += (player.position + displacement) // 40