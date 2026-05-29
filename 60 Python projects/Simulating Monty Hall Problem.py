import random
from random import seed, randint
import numpy as np


def game(winningdoor: int, selecteddoor: int, change: bool = False) -> bool:
    """
    Simulate a single round of the Monty Hall game show.

    Args:
        winningdoor: The door with the car behind it (0, 1, or 2).
        selecteddoor: The door the player initially picks.
        change: Whether the player switches doors after the host reveals a goat.

    Returns:
        True if the player wins the car, False otherwise.
    """
    assert 0 <= winningdoor < 3
    assert 0 <= selecteddoor < 3

    # Host removes a door that was neither selected nor winning
    removeddoor = next(i for i in range(3) if i != selecteddoor and i != winningdoor)

    # Player decides whether to switch to the remaining door
    if change:
        selecteddoor = next(i for i in range(3) if i != selecteddoor and i != removeddoor)

    return selecteddoor == winningdoor


def main():
    """Run a Monte Carlo simulation of the Monty Hall problem."""
    num_trials = 1000 * 1000 * 1  # 1 million trials

    # Use numpy to generate random door choices for the player
    playerdoors = np.random.randint(0, 3, (num_trials,))

    # Count wins without switching
    winningdoors = [d for d in playerdoors if game(1, d)]
    print(f"Winning percentage without changing choice: {len(winningdoors) / len(playerdoors):.4f}")

    # Count wins with switching
    winningdoors = [d for d in playerdoors if game(1, d, change=True)]
    print(f"Winning percentage while changing choice: {len(winningdoors) / len(playerdoors):.4f}")


if __name__ == '__main__':
    main()
