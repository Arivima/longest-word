'''longest_word/game.py'''

from random import choice
from string import ascii_uppercase
from requests import get

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

        found_in_dict = self.__check_dictionary(word)

        return found_in_dict

    @staticmethod
    def __check_dictionary(word):
        try:
            response = get(f'https://dictionary.lewagon.com/{word}', timeout=5)
            response.raise_for_status()
            json_response = response.json()
            return json_response.get('found')
        except Exception as e:
            print({e})
            return False
