"""
Card Game (War).
Two players draw cards from a shuffled deck; the higher card wins each round.
"""

from random import shuffle


class Card:
    """A playing card with a suit and a value."""

    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, value: int, suit: int):
        """suit + value are integers indexing into suits/values lists."""
        self.value = value
        self.suit = suit

    def __lt__(self, other: 'Card') -> bool:
        if self.value < other.value:
            return True
        if self.value == other.value:
            return self.suit < other.suit
        return False

    def __gt__(self, other: 'Card') -> bool:
        if self.value > other.value:
            return True
        if self.value == other.value:
            return self.suit > other.suit
        return False

    def __eq__(self, other: 'Card') -> bool:
        return self.value == other.value and self.suit == other.suit

    def __repr__(self) -> str:
        return f"{self.values[self.value]} of {self.suits[self.suit]}"


class Deck:
    """A deck of 52 playing cards, shuffled on creation."""

    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        """Remove and return the top card. Returns None if empty."""
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


class Player:
    """A player with a name and win count."""

    def __init__(self, name: str):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    """The War card game between two players."""

    def __init__(self):
        name1 = input("Player 1 name: ")
        name2 = input("Player 2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner: str):
        """Print the winner of a round."""
        print(f"{winner} wins this round")

    def draw(self, p1n: str, p1c: Card, p2n: str, p2c: Card):
        """Print what each player drew."""
        print(f"{p1n} drew {p1c} | {p2n} drew {p2c}")

    def play_game(self):
        """Main game loop: draw cards, compare, and track wins."""
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            response = input("q to quit. Any key to play: ")
            if response == 'q':
                break

            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name

            self.draw(p1n, p1c, p2n, p2c)

            if p1c is None or p2c is None:
                break

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            elif p2c > p1c:
                self.p2.wins += 1
                self.wins(self.p2.name)
            else:
                # Tie — both players get a win
                self.p1.wins += 1
                self.p2.wins += 1
                print("It's a tie! Both get a point.")

        winner = self.get_winner(self.p1, self.p2)
        print(f"War is over. {winner}")

    @staticmethod
    def get_winner(p1: Player, p2: Player) -> str:
        """Determine the overall winner based on total wins."""
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"


def main():
    """Start a new game of War."""
    game = Game()
    game.play_game()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame cancelled.")
