from Classes.Tile import BLOCKS
from Classes.Player import Player
from random import randint

class GameManager:
    def __init__(self, game):
        self.game = game

    def game_has_ended(self):
        pass
    
    @classmethod
    def ask_player_for_name(cls):
        return input("What is your name ? ")
    
    def add_player(self):
        name = self.ask_player_for_name()
        self.game.players.append(Player(name))
    
    ######################################
    #### methodes concernant l'argent ####
    ######################################

    @classmethod
    def add_money(cls, player, amount: int):
        player.money += amount

    @classmethod
    def remove_money(cls, player, amount: int):
        player.money -= amount

    @classmethod
    def pay_rent(cls, player1, player2, amount:int):
        cls.remove_money(player1, amount)
        cls.add_money(player2, amount)

    ############################################
    #### methodes concernant les proprietes ####
    ############################################

    @classmethod
    def get_density(cls, terrains):
        return max(terrain.houses_count for terrain in terrains)
    
    @classmethod
    def add_property(cls, player, property):
        if not property in player.properties:
            player.properties.append(property)

    @classmethod
    def remove_property(cls, player, property):
        if property in player.properties:
            player.properties.remove(property)
    
    @classmethod
    def buy_property(cls, player, property):
        if not player.lap_count > 0: return
        if property.owner == None and player.money >= property.price:
            cls.add_property(player, property)
            cls.remove_money(player, property.price)

    @classmethod
    def sell_property(cls, player, property):
        cls.add_money(player, int(0.8*property.price))
        cls.remove_property(player, property)

    @classmethod
    def buy_house(cls, player, terrain):
        if not player.owns_block(terrain.block): return
        block_density = cls.get_density(BLOCKS[terrain.block])
        if terrain.houses_count == block_density:
            for t in BLOCKS[terrain.block]:
                if t.houses_count < block_density: return
        if player.money >= terrain.per_house_price:
            cls.remove_money(player, terrain.per_house_price)
            terrain.build_house()

    @classmethod
    def sell_house(cls, player, terrain):
        if not player.owns_property(terrain) or terrain.houses_count == 0: return
        block_density = cls.get_density(BLOCKS[terrain.block])
        if terrain.houses_count < block_density: return
        terrain.destroy_house()
        cls.add_money(player, int(0.5*terrain.per_house_price))

    ##############################################
    #### methodes concernant les deplacements ####
    ##############################################

    @classmethod
    def roll_dices(cls):
        return (randint(1,6),randint(1,6))
    
    @classmethod
    def move_player(cls, player, displacement: int):
        player.position = (player.position + displacement) % 40
        player.lap_count += (player.position + displacement) // 40