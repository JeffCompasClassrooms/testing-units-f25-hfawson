import unittest
from diceGame import *


class test_diceGame(unittest.TestCase):
    def test_init_basic_parameters(self):
        d = DiceGame()
        self.assertEqual(d.num_players, 2)
        self.assertEqual(d.num_dice, 1)
        self.assertEqual(d.sides_per_die, 6)
        self.assertEqual(d.game_mode, "highest_total")
        self.assertEqual(d.target_score, 50)
        self.assertEqual(d.random_seed, None)

    #the opposite of a value error is not throwing an error
    def test_valid_number_of_players(self):
        DiceGame(num_players=2)
        DiceGame(num_players=3)
        DiceGame(num_players=4)
        DiceGame(num_players=5)
        DiceGame(num_players=6)

    def test_invalid_number_of_players(self):
        self.assertRaises(ValueError, DiceGame, num_players=0)
        self.assertRaises(ValueError, DiceGame, num_players=1)
        self.assertRaises(ValueError, DiceGame, num_players=-1)
        self.assertRaises(ValueError, DiceGame, num_players=7)

    def test_valid_number_of_dice(self):
        DiceGame(num_dice=1)
        DiceGame(num_dice=2)
        DiceGame(num_dice=3)

    def test_invalid_number_of_dice(self):
        self.assertRaises(ValueError, DiceGame, num_dice=0)
        self.assertRaises(ValueError, DiceGame, num_dice=4)
        self.assertRaises(ValueError, DiceGame, num_dice=-1)
    
    def test_valid_sides_per_die(self):
        DiceGame(sides_per_die=2)
        DiceGame(sides_per_die=6)
        DiceGame(sides_per_die=24)

    def test_invalid_sides_per_die(self):
        self.assertRaises(ValueError, DiceGame, sides_per_die=0)
        self.assertRaises(ValueError, DiceGame, sides_per_die=1)
        self.assertRaises(ValueError, DiceGame, sides_per_die=-1)

    def test_valid_game_mode(self):
        DiceGame(game_mode="highest_total")
        DiceGame(game_mode="first_to_target")
        DiceGame(game_mode="all_doubles")

    def test_invalid_game_mode(self):
        self.assertRaises(ValueError, DiceGame, game_mode="")
        self.assertRaises(ValueError, DiceGame, game_mode="highest total")
        self.assertRaises(ValueError, DiceGame, game_mode="first to target")
        self.assertRaises(ValueError, DiceGame, game_mode="doubles")
        self.assertRaises(ValueError, DiceGame, game_mode="random")

    def test_roll_dice(self):
        game = DiceGame()
        for i in range(20):
            roll = game.roll_dice()
            self.assertGreaterEqual(roll[0], 1)
            self.assertLessEqual(roll[0], game.sides_per_die)
'''
sigh im getting a headach trying to figre what these are doing

    def test_play(self):
        game = DiceGame(game_mode="highest_total")
        self.assertEqual(game.play(), game._play_highest_total)



#game modes
    def test_highest_total
        
    def test_first_to_target

    def test_all_doubles

'''
