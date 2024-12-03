from strategy import Strategy
from random import randint

class Random(Strategy):
    """
    The Random Strategy class. This class is when the strategy is simply picking any state at a random order.

    Attributes:
        no_states: Number of possible states.
    """

    def __init__(self, no_states: int = 1) -> None:
        """
        Initialize the random strategy class.

        Attributes:
            no_states: Number of possible states. (Default 1)
        """

        Strategy.__init__(self)
        self.no_states = no_states
    
    def forward(self) -> str:
        """
        Do one forward method depending on the algorithm, and change self.decision.
        """

        random = randint(0, self.no_states)
        self.decision = random