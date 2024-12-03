from random import uniform, randint
from strategy import Strategy
import torch
from torch import Tensor

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

        if probability < self.epsilon:
            self.decision = randint(0, 1)
        else:
            self.decision = int(torch.argmax(self.value))