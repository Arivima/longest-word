# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        new_game = Game()

        # exercise
        grid = new_game.grid
        # verify
        assert isinstance(grid, list)
        assert len(grid) == 9
        for char in grid:
            assert char in string.ascii_uppercase
        # teardown

    def test_empty_word_is_invalid(self):
        new_game = Game()
        assert new_game.is_valid('') is False


    def test_is_valid(self):
        new_game = Game()

        new_game.grid = list('AOYNMLPIYUP')

        assert new_game.is_valid('OLYMPIAN') == True
        assert new_game.grid == list('AOYNMLPIYUP')

    def test_is_invalid(self):
        new_game = Game()

        new_game.grid = list('AOYNLPIYUP')

        assert new_game.is_valid('OLYMPIAN') == False
        assert new_game.grid == list('AOYNLPIYUP')
