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

    def RunEffect(self):
        return

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
    def __init__(self, name: str = "PROPERTY_NAME", price: int = 0, rent: int = 0, owner = None):
        super().__init__(name)
        self.price = price
        self.rent = rent
        self.owner = owner

class Terrain(Property):
    def __init__(self, name: str= "TERRAIN_NAME", rent: int = 0, owner = None, price: int = 0, per_house_price: int = 0, block: str = "BLOCK_NAME"):
        super().__init__(name, rent, owner, price)
        self.houses_count = 0
        self.per_house_price = per_house_price
        self.block = block
    
    def build_house(self):
        self.houses_count += 1

    def destroy_house(self):
        self.houses_count -= 1

class Station(Property):
    def __init__(self, name: str = "STATION_NAME", rent: int = 0, owner = None, price: int = 0):
        super().__init__(name, rent, owner, price)

class PublicService(Property):
    def __init__(self, name: str= "PUBLICSERVICE_NAME", rent: int = 0, owner = None, price: int = 0):
        super().__init__(name, rent, owner, price)
        
BLOCKS = {f"{i}":[Terrain(block = f"{i}")]*(3 if i not in {0, 7} else 2) for i in range(8)}

GYMNASE_EDF = Terrain("GYMNASE_EDF", [2,10,30,90,160,250], None, 60, 50, "BOUYGUES")
MUSEE = Terrain("MUSEE", [4,20,60,180,320,450], None, 60, 50, "BOUYGUES")
AMPHI_I = Terrain("AMPHI_I", [6,30,90,270,400,550], None, 100, 50, "AMPHI_EIFFEL")
AMPHI_II = Terrain("AMPHI_II", [6,30,90,270,400,550], None, 100, 50, "AMPHI_EIFFEL")
AMPHI_III = Terrain("AMPHI_III", [8,40,100,300,450,600], None, 120, 50, "AMPHI_EIFFEL")
TERRASSE_MICHELIN = Terrain("TERRASSE_MICHELIN", [10,50,150,450,625,750], None, 140, 100, "TERRASSES")
TERRASSE_DES_LANGUES = Terrain("TERRASSE_DES_LANGUES", [10,50,150,450,625,750], None, 140, 100, "TERRASSES")
TERRASSE_STUDIO = Terrain("TERRASSE_STUDIO", [12,60,180,500,700,900], None, 160, 100, "TERRASSES")
LA_MAISON_DU_TACOS = Terrain("LA_MAISON_DU_TACOS", [14,70,200,550,750,950], None, 180, 100, "RUE JULES HOROWITZ")
INTERMARCHE = Terrain("INTERMARCHE", [14,70,200,550,750,950], None, 180, 100, "RUE JULES HOROWITZ")
SOCIETE_GENERALE = Terrain("SOCIETE_GENERALE", [16,80,220,600,800,1000], None, 200, 100, "RUE JULES HOROWITZ")
LES_MUSES = Terrain("LES_MUSES", [18,90,250,700,875,1050], None, 220, 150, "CESAL")
RESIDENCE_3 = Terrain("RESIDENCE_3", [18,90,250,700,875,1050], None, 220, 150, "CESAL")
RESIDENCE_4 = Terrain("RESIDENCE_4", [20,100,300,750,925,1100], None, 240, 150, "CESAL")
"""
AMPHI_I = Terrain("AMPHI_1", [22,110,330,800,975,1150], None, 260, 150, "AMPHI_EIFFEL")
AMPHI_I = Terrain("AMPHI_1", [22,110,330,800,975,1150], None, 260, 150, "AMPHI_EIFFEL")         
AMPHI_I = Terrain("AMPHI_1", [24,120,360,850,1025,1200], None, 280, 150, "AMPHI_EIFFEL")
""" # TROUVER UN NOM #
AMPHITHEATRE_ALAIN_ASPECT = Terrain("AMPHITHEATRE_CENTRE_DES_LANGUES", [26,130,390,900,1100,1275], None, 300, 200, "BLOC_AMPHITHEATRE")
AMPHITHEATRE_J_ROUSSEAU = Terrain("AMPHITHEATRE_J_ROUSSEAU", [26,130,390,900,1100,1275], None, 300, 200, "BLOC_AMPHITHEATRE")
AUDITORIUM_MICHELIN = Terrain("AUDITORIUM_MICHELIN", [28,150,450,1000,1200,1400], None, 320, 200, "BLOC_AMPHITHEATRE")
RESIDENCE_5 = Terrain("RESIDENCE_5", [35,175,500,1100,1300,1500], None, 350, 200, "RESIDENCES_RICHES")
RESIDENCE_6 = Terrain("RESIDENCE_6", [50,200,600,1400,1700,2000], None, 400, 200, "RESIDENCES_RICHES")


STATION_JOLIOT_CURIE = Station("STATION_JOLIOT_CURIE", [25,50,100,200], None, 200)
STATION_MOULON = Station("STATION_MOULON", [25,50,100,200], None, 200)
GARE_DU_GUICHET = Station("GARE_DU_GUICHET", [25,50,100,200], None, 200)
GARE_DE_MASSY_PALAISEAU = Station("GARE_DE_MASSY_PALAISEAU", [25,50,100,200], None, 200)


CROUS_EIFFEL = PublicService("CROUS_EIFFEL", [4,10], None, 150)
CROUS_ENS = PublicService("CROUS_ENS", [4,10], None, 150)

