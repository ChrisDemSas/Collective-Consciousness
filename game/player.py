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
        healing_factor: The healing factor of the player.
        crit_factor: The critical hit chance of the player.
    """

    def __init__(self, hp: int, attack: int, magic: int, defence: int, strategy = None) -> None:
        """Take in a hp, attack and magic skill point and initialize the class.
        
        Attributes:
            hp: The number of hp the player starts with.
            attack: The number of attack points the player starts with.
            magic: The number of magic points the player starts with.
            strategy: The strategy of the player, either 'Random' for Random Choices, 'RL' for Reinforcement Learning or None (For Player).
        """

        self.hp = 100 + hp
        self.attack = 1 + attack
        self.magic = 1 + magic
        self.defence = 1 + defence
        self.current_action = None
        self.strategy = strategy
        self.buffs = {'physical': 1, 'magic_defence': 1, 'magic': 1, 'physical_defence': 1}  
        self.crit_factor = 1
        self.healing_factor = 1
        self.crit = 1
    
    def _physical_attack(self) -> float:
        """Calculate the attack of a physical attack.
        """

        return self.buffs['physical'] * self.attack * self.crit

    def _magic_attack(self) -> float:
        """Calculate the attack of a magic attack.
        """

        return self.buffs['magic'] * self.magic * self.crit

    def _heal(self) -> float:
        """Calculate the healing.

        Attributes:
            healing_factor: The healing factor for the self heal.
        """

        return self.buffs['magic'] * (self.healing_factor / self.hp) * 100
    
    def _crit(self) -> int:
        """Checks to see if there is a critical hit during this turn.

        Attributes:
            crit_factor: The critical factor for calculating if this turn is a critical hit.
        """

        crit_chance = self.crit_factor * 0.05
        crit_no = random.uniform(0, 1) 

        if crit_no > crit_chance:
            self.crit = 2 

    def turn(self, attributes: json) -> float:
        """Take in a bunch of attributes and update parameters. 

        Pre-Condition: Attributes JSON:
            {
                "attack_type": "Magic" or "Physical",
                "attack_used": "Attack", "Fireball" or "Defence Up" or "Attack Up"
            }
        
        Attributes:
            attributes: A JSON file which contains the attributes of the attack.
        """

        attack_type = attributes['attack_type']
        attack_used = attributes['attack_used']
        self._crit()

        if attack_used == "Physical":
            return self._physical_attack()
        elif attack_used == "Fireball":
            return self._magic_attack()
        elif attack_used == "Defence Up":
            if attack_type == 'Physical':
                self.buffs["physical_defence"] += 1
            elif attack_type == "Magic":
                self.buffs['magic_defence'] += 1
        elif attack_used == "Attack Up":
            if attack_type == "Physical":
                self.buffs['physical'] += 1
            elif attack_type == "Magic":
                self.buffs['magic'] += 1
        
        self.reset_crit()

    def take_damage(self, damage_taken: float) -> None:
        """Take in a damage number and reduce self.hp.
        
        Attributes:
            damage_taken: The total number of damage taken.
        """

        self.hp -= damage_taken

    def show_hp(self) -> float:
        """Return self.hp. 
        """

        return self.hp
    
    def show_buffs(self) -> dict:
        """Return self.buffs.
        """

        return self.buffs
    
    def reset_crit(self) -> None:
        """Reset the crit chance.
        """

        self.crit = 1
    
    def check_game_over(self) -> str:
        """Checks to see if self.hp <= 0. If it is, return "Game Over".
        """

        if self.hp <= 0:
            return "Game Over"
        else:
            return "Continue"