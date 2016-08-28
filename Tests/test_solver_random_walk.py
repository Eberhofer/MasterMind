import unittest

from MasterMind.game import Game
from MasterMind.solvers import random_walk

class TestSolverRandom(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_solution_is_correct(self):
        self.assertEqual(random_walk.random_walk(self.game)[0],
                [self.game.colordict[self.game.challenge[i]] for i in self.game._slots])

if __name__ == '__main__':
    unittest.main()
