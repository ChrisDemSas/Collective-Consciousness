# Implementation of the game board class
from player import Player
import json

class Gameboard:
    """Implementation of the Player Class.
    
    Attributes:
        player: A player of the game.
        stats: Attributes of the stats.
        turn_history: A history of the turns used by Players.
        turn_number: Turn number.
        winner: The victor of the game.
    """

    def __init__(self, player_one: Player, player_two: Player) -> None:
        """Take in a player and initialize the class.

        Attributes:
            player_one: An initialized player one of the game.
            player_two: An initialized player two of the game.
        """

        self.player_one = player_one
        self.player_two = player_two
        self.turn_number = 0
        self.turn_history = []
        self.winner = []

    def take_turn(self, player_number: int) -> None:
        """Take a turn for the player and update the player's parameter.

        Attributes:
            player_number: The player number (Either 1 or 2).
        """
    
    def choose_action(self, action: json) -> None:
        """Take in an action and calculate the impact.
        
        Attributes:
            action: The player's action.
        """