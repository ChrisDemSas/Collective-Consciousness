from random import uniform, randint
from strategy import Strategy

class EpsilonGreedy(Strategy):
    """
    Implementation of the Epsilon Greedy Algorithm.
    
    Attribute:
        epsilon: The Epsilon value which controls degree of exploration.
    """

    def __init__(self, epsilon: float) -> None:
        """
        Initialize the EpsilonGreedy class.

        Attributes:
            epsilon: The Epsilon value which controls degree of exploration.
        """

        Strategy.__init__()
        
        self.epsilon = epsilon
    
    def forward(self) -> None:
        """
        Create one forward iteration for the Epsilon Greedy Algorithm.
        """

        probability = uniform(0, 1)

        if probability < (1 - self.epsilon):
            random_data = randint(0, 1)
        else:
            

