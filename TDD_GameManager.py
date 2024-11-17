from Classes.Player import Player
from Classes.Game import Game
from Classes.GameManager import GameManager

game = Game()

def test_add_money():
    game.players.append(Player(game))
    player = game.players[0]
    GameManager.add_money(player, 100)
    assert player.money == 100

test_add_money()

