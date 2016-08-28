import unittest

from MasterMind.game import Game
from MasterMind.solvers import brute_force

class TestSolverBruteForce(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_solution_is_correct(self):
        self.assertEqual(brute_force.brute_force(self.game)[0],
                        [self.game.colordict[self.game.challenge[i]] for i in self.game._slots])

if __name__ == '__main__':
    unittest.main()
