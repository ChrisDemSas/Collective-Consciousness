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
        buffs: A dictionary keeping track of the player's buffs.
        crit: Critical hit.
    """

    def __init__(self, hp: int, attack: int, magic: int, defence: int, strategy = None) -> None:
        """Take in a hp, attack and magic skill point and initialize the class.
        
        Attributes:
            hp: The number of hp the player starts with.
            attack: The number of attack points the player starts with.
            magic: The number of magic points the player starts with.
            strategy: The strategy of the player, either 'Random' for Random Choices, 'RL' for Reinforcement Learning or None (For Player).
        """

        self.hp = 1 + hp
        self.attack = 1 + attack
        self.magic = 1 + magic
        self.defence = 1 + defence
        self.current_action = None
        self.strategy = strategy
        self.buffs = {'physical': 1, 'defence': 1, 'magic': 1}  
        self.crit = 1      
    
    def _physical_attack(self) -> float:
        """Calculate the attack of a physical attack.
        """

        return self.buffs['physical'] * self.attack * self.crit

    def _magic_attack(self) -> float:
        """Calculate the attack of a magic attack.
        """

        return self.buffs['magic'] * self.magic * self.crit

    def _heal(self, healing_factor: float) -> float:
        """Calculate the healing.

        Attributes:
            healing_factor: The healing factor for the self heal.
        """

        return self.buffs['magic'] * (healing_factor / self.hp) * 100 * self.crit
    
    def _crit(self, crit_factor: float = 1) -> int:
        """Checks to see if there is a critical hit during this turn.

        Attributes:
            crit_factor: The critical factor for calculating if this turn is a critical hit.
        """

        crit_chance = crit_factor * 0.05
        crit_no = random.uniform(0, 1) 

        if crit_no > crit_chance:
            self.crit = 2
        

    def calculate_damage(self, attributes: json) -> float:
        """Take in a bunch of attributes and calculate the damage. 

        Pre-Condition: Attributes JSON:
            {
                "attack_type": "Magic" or "Physical" or "Shield", 
                "attack_used": "Physical" or "Heal" or "Defence Up", "Attack Up", "Shield", "Magic"
                "critical": "Yes" or "No
             }
        
        Attributes:
            attributes: A JSON file which contains the attributes of the attack.
        """

        crit = random.uniform(0, 1)

        
    def show_hp(self) -> float:
        """Return self.hp. """

        return self.hp
    
    def show_buffs(self) -> dict:
        """Return self.buffs."""

        return self.buffs
    
    def reset_crit(self) -> None:
        """Reset the crit chance."""

        self.crit = 1