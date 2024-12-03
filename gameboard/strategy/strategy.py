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

        return self.decision