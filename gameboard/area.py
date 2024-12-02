from gameboard_helper import initialize_gameboard
from random import randint
from species import Species

class Area:
    """
    The Area class where the population will live in.
    
    Attributes:
        population: The total number of species.
        episodes: The total episodes until the experiment finishes.
        gameboard: The gameboard.
        width: The width of the gameboard.
        height: The height of the gameboard.
        states: All of the states of the gameboard.
    """

    def __init__(self, species: Species, population: int, episodes: int, width: int, height: int) -> None:
        """
        Initialize the Area class.

        Attributes:
            population: The total number of species.
            episodes: The total episodes until the experiment finishes.
            width: The width of the gameboard.
            height: The height of the gameboard.
        """

        self.population = population
        self.episodes = episodes
        self.gameboard = initialize_gameboard(width, height)
        self.states = []
        self.species = species
    
    def randomize_positions(self) -> None:
        """
        Randomly put species inside the gameboard in a random manner.
        """

        tracker = 0
        done_data = []

        while tracker != self.population:

            random_y = randint(0, len(self.gameboard))
            random_x = randint(0, len(self.gameboard[0]))
            if not ((random_x, random_y) in done_data):
                self.gameboard[random_y][random_x] = self.species 
                done_data.append((random_x, random_y))

                tracker += 1
    
    def erase(self, x: int, y: int) -> None:
        """
        Take in a coordinate (x and y) and replace the item with a 0.
        """

        self.gameboard[y][x] = 0
    
    def move_species(self) -> None:
        """
        For each of the species in the gameboard, generate a random number so that it can move.
        """

        pass
    
    def save_state(self) -> None:
        """
        Save the current gameboard in self.states.
        """

        self.states.append(self.gameboard)
    
    def battle(self, spec) -> None:
        """
        Do one turn of battling.
        """

        pass