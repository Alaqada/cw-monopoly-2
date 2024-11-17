from Classes.GameManager import GameManager
from Classes.Game import Game
from Classes.Player import Player

game = Game()

def test_add_money():
    player = Player(game)
    GameManager.add_money(player, 100)
    assert player.money != 100

test_add_money

