from random import sample, choice
from itertools import product, combinations
from functools import reduce
#import numpy as np
from collections import Counter

class Game:
    _colors = set('red blue yellow green orange brown'.split(' '))
    _slots = range(4)

    def _create_colordict(self, cn, colorset):
        """
            creates a dict of the chars used internally to the availlable collors

            >>> sorted(Game()._create_colordict('vwxyz', {'magenta', 'coral', 'peach', 'navy', 'maroon'}).keys())
            ['v', 'w', 'x', 'y', 'z']

            >>> sorted(Game()._create_colordict('vwxyz', {'magenta', 'coral', 'peach', 'navy', 'maroon'}).values())
            ['coral', 'magenta', 'maroon', 'navy', 'peach']

            Note that the dict is actually sorted in arbitrary ways, so the interesting result is
            the keys or the values - at least if the input is a set.

            >>> sorted(Game()._create_colordict('vwxyz', ['magenta', 'coral', 'peach', 'navy', 'maroon']).items())
            [('v', 'magenta'), ('w', 'coral'), ('x', 'peach'), ('y', 'navy'), ('z', 'maroon')]

            If a list is passed, then the keys are assigned to values in a predictable fashion and
            it makes sense to test for the ordered dict.
        """
        return dict(zip(cn, colorset))

    def __init__(self, slots = None, colors = None):
        if slots is not None:
            self._slots = range(slots)
        if colors is not None:
            self._colors = set(colors.split(' '))
        self._colorchars = 'abcdefghijklmnopqrstuvwxyz'[:len(self._colors)]
        self.colordict = self._create_colordict(self._colorchars, self._colors)
        self.set_challenge()

    def set_challenge(self,solution_set=None):
        self.challenge = self.create_code(solution_set)

    def create_code(self,solution_set=None):
        if solution_set is None:
            newcode = ''.join(choice(self._colorchars) for _ in self._slots)
        else:
            newcode = choice(solution_set)
        return newcode

    def evaluator(self, trial, benchmark = None):
        if benchmark is None:
            benchmark = self.challenge
        blackandwhite = sum((Counter(trial) & Counter(benchmark)).values())
        black = sum(a == b for a,b in zip(trial, benchmark))
        white = blackandwhite - black
        return black, white

# aux methods for solvers
    def create_solution_generator(self):
        return product(self._colorchars, repeat=len(self._slots))

    def reduce_solution_set(self,solution_set,trial,result):
        yield from (i for i in solution_set if self.evaluator(i,trial) == result)

    def binomial_coeff(n,k):
        if n<k:
            raise ValueError('k > n is not allowed in binomial_coeff(n,k).')
        if type(n) != int or type(k) != int:
            raise ValueError('binomial_coeff(n,k) is only defined for integer n and k.')
        return int(factorial(n)/(factorial(k) * factorial(n-k)))
