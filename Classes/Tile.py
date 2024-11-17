from abc import ABC, abstractmethod

class Tile(ABC):
    def __init__(self, name: str = "TILE_NAME"):
        self.name = name

class EffectTile(Tile, ABC):
    def __init__(self, name: str = "EFFECT_TILE_NAME"):
        super().__init__(name)
        
    @abstractmethod
    def RunEffect(self):
        pass

class Luck(EffectTile):
    def __init__(self):
        super().__init__("Case chance")

class Community(EffectTile):
    def __init__(self):
        super().__init__("Caisse de la communauté")

class StartingTile(EffectTile):
    def __init__(self):
        super().__init__("Départ")

class Parc(EffectTile):
    def __init__(self):
        super().__init__("Parc gratuit")

class Arrest(EffectTile):
    def __init__(self):
        super().__init__("Allez en prison")

class Taxe(EffectTile):
    def __init__(self):
        super().__init__("Taxe")

class Prison(Tile):
    def __init__(self):
        super().__init__("Prison")

class Property(Tile, ABC):
    def __init__(self, name: str = "PROPERTY_NAME", price: int = 0, rent: int = 0, owner: "Player" = None):
        super().__init__(name)
        self.price = price
        self.rent = rent
        self.owner = owner

class Terrain(Property):
    def __init__(self, name: str= "TERRAIN_NAME", rent: int = 0, owner: "Player" = None, price: int = 0, per_house_price: int = 0, block: str = "BLOCK_NAME"):
        super().__init__(name, rent, owner, price)
        self.houses_count = 0
        self.per_house_price = per_house_price
        self.block = block
    
    def build_house(self):
        self.houses_count += 1

    def destroy_house(self):
        self.houses_count -= 1

class Station(Property):
    def __init__(self, name: str = "STATION_NAME", rent: int = 0, owner: "Player" = None, price: int = 0):
        super().__init__(name, rent, owner, price)

class PublicService(Property):
    def __init__(self, name: str= "PUBLICSERVICE_NAME", rent: int = 0, owner: "Player" = None, price: int = 0):
        super().__init__(name, rent, owner, price)
        
BLOCKS = {f"{i}":[Terrain(block = f"{i}")]*(3 if i not in {0, 7} else 2) for i in range(8)}
