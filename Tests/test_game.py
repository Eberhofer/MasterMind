import unittest

from MasterMind.game import Game
from MasterMind.solvers import random_walk

class TestConstruction(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_colors(self):
        self.assertEqual(self.game._colors, set(['blue', 'green', 'yellow', 'orange', 'red', 'brown']))

    def test_slots(self):
        self.assertEqual(self.game._slots, range(4))

    def test_init(self):
        for i in self.game._slots:
            self.assertTrue(self.game.challenge[i] in self.game._colorchars)

class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_challenge_evaluates_correctly(self):
        self.assertEqual(self.game.evaluator(self.game.challenge), (4,0))

    def test_benchmark_evaluates_(self):
        self.assertEqual(self.game.evaluator([1,2,3,4], [1,3,6,2]), (1,2))

class TestCreateSolution(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_len_solution_generator(self):
        s = [i for i in self.game.create_solution_generator()]
        self.assertEqual(len(s), len(self.game._colors) ** len(self.game._slots))

if __name__ == '__main__':
    unittest.main()
