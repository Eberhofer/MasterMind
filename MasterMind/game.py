"""
    game.py defines the MasterMind Game class.
"""
from random import choice
from itertools import product
from collections import Counter

class Game:
    """
        The Game class provides MasterMind game class and methods
        that can be used by various testing strategies.
    """
    _colors = set('red blue yellow green orange brown'.split(' '))
    _slots = range(4)

    def _create_colordict(self):
        """
            creates a dict of chars to available colors

            >>> sorted(Game()._create_colordict('vwxyz',
                {'magenta', 'coral', 'peach', 'navy', 'maroon'}).keys())
            ['v', 'w', 'x', 'y', 'z']

            >>> sorted(Game()._create_colordict('vwxyz',
                {'magenta', 'coral', 'peach', 'navy', 'maroon'}).values())
            ['coral', 'magenta', 'maroon', 'navy', 'peach']

            Note that the dict is actually sorted in arbitrary ways, so the
            interesting result is the keys or the values - at least if the
            input is a set.

            >>> sorted(Game()._create_colordict('vwxyz',
                ['magenta', 'coral', 'peach', 'navy', 'maroon']).items())
            [('v', 'magenta'), ('w', 'coral'), ('x', 'peach'), ('y', 'navy'), ('z', 'maroon')]

            If a list is passed, then the keys are assigned to values in a
            predictable fashion and it makes sense to test for an ordered dict.
        """
        return dict(zip(self._colorchars, self._colors))

    def __init__(self, slots=None, colors=None):
        if slots is not None:
            self._slots = range(slots)
        if colors is not None:
            self._colors = set(colors.split(' '))
        self._colorchars = 'abcdefghijklmnopqrstuvwxyz'[:len(self._colors)]
        self.colordict = self._create_colordict()
        self.set_challenge()

    def set_challenge(self, solution_set=None):
        """
            Sets the challenge property with the possibility
            to restrict the codes to a custom solution_set.
        """
        self.challenge = self.create_code(solution_set)

    def create_code(self, solution_set=None):
        """
            Creates a random code from a solution_set.
            By default the unrestricted set is used.
        """
        if solution_set is None:
            newcode = ''.join(choice(self._colorchars) for _ in self._slots)
        else:
            newcode = choice(solution_set)
        return newcode

    def evaluator(self, trial, benchmark=None):
        """
            Returns the evaluation of a trial vs a benchmark.
            self.challenge is used as default benchmark.
        """
        if benchmark is None:
            benchmark = self.challenge
        blackandwhite = sum((Counter(trial) & Counter(benchmark)).values())
        black = sum(a == b for a, b in zip(trial, benchmark))
        white = blackandwhite - black
        return black, white

# aux methods for solvers
    def create_solution_generator(self):
        """
            returns a generator for all solutions of self.
        """
        return product(self._colorchars, repeat=len(self._slots))

    def reduce_solution_set(self, solution_set, trial, evaluation):
        """
            returns a generator for all solutions in solution_set that
            are still possible based on trial and its evaluation.
        """
        yield from (i for i in solution_set
                    if self.evaluator(i, trial) == evaluation)

    def create_feedback_dict(self):
        """
            returns a dict containing tuples of two codes as key and their
            evalution as value.
        """
        gen1 = self.create_solution_generator()
        gen2 = self.create_solution_generator()
        return dict([((''.join(i), ''.join(j)), self.evaluator(i, j)) for i, j in zip(gen1, gen2)])
