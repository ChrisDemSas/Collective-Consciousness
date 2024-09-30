# Implementation of the Player Class.
import json
import random

class Player:
    """Implementation of the Player Class.
    
    Attributes:
        hp: The number of hp the player starts with.
        attack: The number of attack points the player starts with.
        magic: The number of magic points the player starts with.
        current_action: The action of the player.
        strategy: The strategy of the player.
    """

    def __init__(self, hp: int, attack: int, magic: int, defence: int, strategy = None) -> None:
        """Take in a hp, attack and magic skill point and initialize the class.
        
        Attributes:
            hp: The number of hp the player starts with.
            attack: The number of attack points the player starts with.
            magic: The number of magic points the player starts with.
            strategy: The strategy of the player, either 'Random' for Random Choices, 'RL' for Reinforcement Learning or None.
        """

        self.hp = 1 + hp
        self.attack = 1 + attack
        self.magic = 1 + magic
        self.defence = 1 + defence
        self.current_action = None
        self.strategy = strategy
        self.buffs = {'physical': 0, 'defence': 0, 'magic': 0}        
    
    def _physical_attack(self) -> float:
        """Calculate the attack of a physical attack.
        """

        pass

    def _magic_attack(self) -> float:
        """Calculate the attack of a magic attack.
        """

        pass

    def _heal(self) -> float:
        """Calculate the healing.
        """

        pass

    def calculate_damage(self, attributes: json) -> float:
        """Take in a bunch of attributes and calculate the damage. 

        Pre-Condition: Attributes JSON:
            {
                "attack_type": "Magic" or "Physical" or "Shield", 
                "attack_used": "Physical" or "Heal" or "Defence Up", "Attack Up", "Shield",
                "critical": "Yes" or "No
             }
        
        Attributes:
            attributes: A JSON file which contains the attributes of the attack.
        """

        pass

    def show_hp(self) -> float:
        """Return self.hp. """

        return self.hp
    
    def show_buffs(self) -> dict:
        """Return self.buffs."""

        return self.buffs