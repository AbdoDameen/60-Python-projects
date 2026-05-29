"""
Chessboard Visualization.
Creates a chessboard pattern using matplotlib with an overlaid gradient.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def chess_pattern(x: float, y: float) -> float:
    """
    Compute a gradient function used to overlay on the chessboard.
    """
    return (1 - x / 2 + x**5 + y**6) * np.exp(-(x**2 + y**2))


def main():
    """Generate and display a chessboard with a gradient overlay."""
    dx, dy = 0.015, 0.05
    x = np.arange(-4.0, 4.0, dx)
    y = np.arange(-4.0, 4.0, dy)
    X, Y = np.meshgrid(x, y)

    # Create chessboard pattern
    z1 = np.add.outer(range(8), range(8)) % 2
    extent = (x.min(), x.max(), y.min(), y.max())
    plt.imshow(z1, cmap="binary_r", interpolation="nearest",
               extent=extent, alpha=1)

    # Overlay gradient
    z2 = chess_pattern(X, Y)
    plt.imshow(z2, alpha=0.6, interpolation="bilinear",
               extent=extent)

    plt.title("CHESS BOARD")

    # Use multiples of 1 for tick marks
    loc = MultipleLocator(base=1.0)
    plt.yticks(loc)
    plt.xticks(loc)

    plt.show()


if __name__ == '__main__':
    main()
