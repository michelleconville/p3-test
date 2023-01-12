import random

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def get_random_word():
    """
    Picks a random word from words.txt
    """
    random_word = random.choice(open("words.txt").read().split('\n'))
    return random_word.upper()

def main():
    """
    Runs the game 
    """
    game_word = get_random_word()
    print("Lets play hangman!")


main()