# Implementation of the game board class
from player import Player
import json

class Gameboard:
    """Implementation of the Player Class.
    
    Attributes:
        player: A player of the game.
        turn_history: A history of the turns used by Players.
    """

    def __init__(self, player: Player) -> None:
        """Take in a player and initialize the class.

        Attributes:
            player: A player of the game.
        """

        self.player = Player()