import unittest

from MasterMind.game import Game

class TestConstruction(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_colors(self):
        self.assertEqual(self.game._colors, set(['blue', 'green', 'yellow', 'orange', 'red', 'brown']))

    # def test_slots(self):
    #     g = Game()
    #     g._slots == [0, 1,2,3]
    #
    # def test_init(self):
    #     g = Game()
    #     print(g.challenge)
    #     for i in g._slots:
    #         g.challenge[i] in g._colornumbers

# class TestEvaluator(unittest.TestCase):
#     def test_challenge_evaluates_correctly(self):
#         g = Game()
#         g.evaluator(g.challenge) == (4,0)
#
#     def test_benchmark_evaluates_(self):
#         g = Game()
#         g.evaluator([1,2,3,4], [1,3,6,2]) == (1,2)
#
# class TestCreateSolution(unittest.TestCase):
#     def test_len_solution_set(self):
#         g = Game()
#         s = g.create_solution_set()
#         len(s) == len(g._colors)^4
#
# class TestSolverRandom(unittest.TestCase):
#     def test_solution_is_correct(self):
#         g = Game()
#         g.solver_random()[0] == g.challenge
#
# class TestSolverBruteForce(unittest.TestCase):
#     def test_solution_is_correct(self):
#         g = Game()
#         g.solver_brute_force()[0] == g.challenge
#
# class TestSolverBySlot(unittest.TestCase):
#     def test_solution_is_correct(self):
#         g = Game()
#         self.assertEqual(g.solver_by_slot(), g.challenge)


if __name__ == '__main__':
    unittest.main()
