from typing import List


class GameOfLife:
    """Conway's Game of Life simulation on a 2D board."""

    # The 8 possible neighbor offsets (row, col)
    NEIGHBORS: List[tuple[int, int]] = [
        (1, 0), (1, -1), (0, -1), (-1, -1),
        (-1, 0), (-1, 1), (0, 1), (1, 1),
    ]

    def game_of_life(self, board: List[List[int]]) -> None:
        """
        Apply one step of Conway's Game of Life to the board in-place.

        Rules:
        1. Any live cell with <2 live neighbors dies (under-population).
        2. Any live cell with 2 or 3 live neighbors lives on.
        3. Any live cell with >3 live neighbors dies (over-population).
        4. Any dead cell with exactly 3 live neighbors becomes alive (reproduction).

        Args:
            board: A 2D list of 0s (dead) and 1s (alive). Modified in place.
        """
        rows = len(board)
        columns = len(board[0])

        # Create a deep copy of the board to track the original state
        copy_board = [[board[row][col] for col in range(columns)] for row in range(rows)]

        for row in range(rows):
            for col in range(columns):
                live_neighbors = 0

                # Count live neighbors
                for dr, dc in self.NEIGHBORS:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < rows and 0 <= c < columns and copy_board[r][c] == 1:
                        live_neighbors += 1

                # Apply Game of Life rules
                # (use copy_board for the original state, write results to board)
                if copy_board[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][col] = 0  # Cell dies
                else:
                    if live_neighbors == 3:
                        board[row][col] = 1  # Cell becomes alive


def print_board(board: List[List[int]]) -> None:
    """Print the board with visual characters for alive/dead cells."""
    for row in board:
        print(' '.join('#' if cell else '.' for cell in row))
    print()


def main():
    """Demonstrate Conway's Game of Life with a simple test pattern."""
    # Glider pattern — a classic Game of Life oscillator
    initial_board: List[List[int]] = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    game = GameOfLife()

    print("Initial board:")
    print_board(initial_board)

    # Run 5 generations
    for gen in range(1, 6):
        game.game_of_life(initial_board)
        print(f"Generation {gen}:")
        print_board(initial_board)


if __name__ == '__main__':
    main()
