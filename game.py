from random import sample, choice
from itertools import product, combinations
from functools import reduce
import numpy as np
from collections import Counter

class Game:
    _colors = set('red blue yellow green orange brown'.split(' '))
    _slots = np.arange(4)

    def _create_colordict(colorset):
        cn = 'abcdefghijklmnopqrstuvwxyz'[:len(colorset)]
        return dict(zip(cn, colorset))

    def __init__(self, slots = None, colors = None):
        if slots is not None:
            self._slots = np.arange(slots)
        if colors is not None:
            self._colors = set(colors.split(' '))
        self._colorchars = 'abcdefghijklmnopqrstuvwxyz'[:len(self._colors)]
        charlist = [self._colorchars[i] for i in range(len(self._colors))]
        self._colordict = dict(zip(self._colorchars, self._colors))
        self.challenge = self.create_code()

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
        return np.array([i for i in solution_set if self.evaluator(i,trial) == result])

    def binomial_coeff(n,k):
        if n<k:
            raise ValueError('k > n is not allowed in binomial_coeff(n,k).')
        if type(n) != int or type(k) != int:
            raise ValueError('binomial_coeff(n,k) is only defined for integer n and k.')
        return int(factorial(n)/(factorial(k) * factorial(n-k)))
