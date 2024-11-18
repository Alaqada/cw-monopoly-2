from Classes.Board import Board
from Classes.GameManager import GameManager

class Game:
    def __init__(self):
        self.board = Board(self)
        self.players = []
        self.game_manager = GameManager(self)
    
    def start(self, player_count=4):
        # Players join the game
        for _ in range(player_count):
            self.game_manager.add_player()
        # Game loop starts
        while not GameManager.game_has_ended():
            for player in self.game.players:
                player.play()
        # Winner winner chiken dinner
        winner = None
        for player in self.game.players:
            if not player.is_bankrupt():
                winner = player
                break