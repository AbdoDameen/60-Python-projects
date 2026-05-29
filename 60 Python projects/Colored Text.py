"""
Colored Text example.
Demonstrates using the colorama library to print colored text in the terminal.
"""

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def main():
    """Print several examples of colored text."""
    # Example: user can customize these variables
    name = "Abdo"
    title = "Data Science Student"

    print(f"{Fore.BLUE}{Back.YELLOW}Hi, my name is {name} {Fore.BLUE}{Back.YELLOW}I am a {title}")
    print(f"{Back.CYAN}Hi, my name is {name}")
    print(f"{Fore.RED}{Back.GREEN}Hi, I'm still here")
    print(f"{Fore.GREEN}{Back.BLACK}This is another colored message example")
    print(f"{Fore.MAGENTA}{Back.WHITE}Colored text is fun with colorama!")


if __name__ == '__main__':
    main()
