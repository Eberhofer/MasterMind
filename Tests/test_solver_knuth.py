import unittest

from MasterMind.game import Game
from MasterMind.solvers import knuth

class TestSolverBruteForce(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    @unittest.skip("********** knuth test takes too long - only run when knuth is changed **********")
    def test_solution_is_correct(self):
        self.assertEqual(knuth.knuth(self.game)[0],
                        [self.game.colordict[self.game.challenge[i]] for i in self.game._slots])

if __name__ == '__main__':
    unittest.main()
