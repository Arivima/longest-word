'''longest_word/game.py'''

from random import choice
from string import ascii_uppercase


class Game:
    """Game class"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(choice(ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        grid = self.grid.copy() # Consume letters from the grid
        for c in word:
            if c not in grid:
                return False
            grid.remove(c)
        return True
