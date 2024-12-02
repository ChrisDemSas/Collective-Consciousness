def initialize_gameboard(width: int, height: int) -> list:
    """
    Take in the width and height of the gameboard and initialize the gameboard.

    Attributes:
        width: The width of the gameboard.
        height: The height of the gameboard.
    """

    gameboard = []

    for i in range(0, height):
        final = []

        for j in range(0, width):
            final.append(0)

        gameboard.append(final)
    
    return gameboard