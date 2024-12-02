from random import randint

class Species:
    """
    The Species class: A species which can move, fight, etc.

    Attributes:
        position: The current position of the species.
        strategy: The strategy being used by the species.
        hp: The total hit points of the species (0 = dead)
        data: The past states of the species.

    """

    def __init__(self, strategy: str, initial_position: tuple, hp: int = 5) -> None:
        """
        Initialize the Species class.

        Attributes:
            strategy: The strategy for the Species Class.
            initial_position: The initial position of each species.
        """

        self.strategy = strategy
        self.position = initial_position
        self.hp = hp
        self.data = []
    
    def move(self, number: int) -> None:
        """
        Take in a randomized number and then update the position if the number is 1 and non-update if the number is 0.
        
        Attributes:
            number: The randomized number to update the position.
        """

        if number == 1:
            self.position[0] += 1
        
        elif number == 2:
            self.position[1] += 1

        elif number == 3:
            self.position[0] -= 1
        
        elif number == 4:
            self.position[1] -= 1
    
    def act(self) -> str:
        """
        Use the strategy to give an outcome for the Species.
        """

        raise NotImplementedError
    
    def update_health(self, verdict: str) -> None:
        """
        Increment health by 1 if verdict is "Won", decrement health by 1 if verdict is "Loss", Otherwise do nothing.
        """

        if verdict == "Won":
            self.health += 1
        elif verdict == "Loss":
            self.health -= 1