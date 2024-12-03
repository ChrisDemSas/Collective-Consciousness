import torch
from torch import Tensor

class Strategy:
    """
    Initialize the Strategy class.
    """

    def __init__(self) -> None:
        """
        Initialize the Strategy Class.
        """

        self.value = torch.Tensor([0, 0])
        self.states = {0: "Defect", 1: "Cooperate"}
        self.decision = None

    def forward(self) -> str:
        """
        Do one forward method depending on the algorithm, and change self.decision.
        """

        raise NotImplementedError
    
    def return_decision(self) -> str:
        """
        Return self.decision.
        """

        return self.states[self.decision]
    
    def _update_value_function(self, decision: int, reward: int, episodes: int) -> None:
        """
        Take in a step size and then update the value function by taking in a decision (helper)
        """

        self.value[decision] += (1/episodes) * (reward - self.value[decision])
    
    def update_value_function(self, opponent_decision: int, decision: int, episodes: int) -> None:
        """
        Take in a step size and then update the value function by taking in a decision.
        """

        if (opponent_decision == 1) and (decision == 1): # Coop-Coop
            self._update_value_function(opponent_decision, self.decision, 2, episodes)
        elif (opponent_decision == 1) and (decision == 0): #Coop - Defect
            self._update_value_function(opponent_decision, self.decision, 3, episodes)
        elif (opponent_decision == 0) and (decision == 1): #Defect - Coop
            self._update_value_function(opponent_decision, self.decision, -1, episodes)
        elif (opponent_decision == 0) and (decision == 0): #Defect - Defect
            self._update_value_function(opponent_decision, self.decision, 0, episodes)