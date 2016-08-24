from random import sample, choice
from itertools import product, combinations
from functools import reduce
import numpy as np
from collections import Counter

def knuth(secret):
    """Run Knuth's 5-guess algorithm on the given secret.
        from http://stackoverflow.com/questions/20298190/mastermind-minimax-algorithm
    """
    ALL_CODES
    assert(secret in ALL_CODES)
    codes = ALL_CODES
    key = lambda g: max(Counter(evaluate(g, c) for c in codes).values())
    guess = 'AABB'
    while True:
        feedback = evaluate(guess, secret)
        print("Guess {}: feedback {}".format(guess, feedback))
        if guess == secret:
            break
        codes = [c for c in codes if evaluate(guess, c) == feedback]
        if len(codes) == 1:
            guess = codes[0]
        else:
            guess = min(ALL_CODES, key=key)

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

# solvers
    def solver_random(self):
        trial = []
        n = 0
        while trial != self.challenge:
            trial = self.create_code()
            #print(trial)
            n += 1
        return trial, n

    def solver_brute_force(self):
        s = np.array([''.join(c) for c in self.create_solution_generator()])
        n = 0
        print('n {} and len(s) {}'.format(n,len(s)))
        while len(s) > 1:
            trial = self.create_code(s)
            result = self.evaluator(trial)
            s = self.reduce_solution_set(s, trial, result)
            n += 1
            print('n {} and len(s) {} after trial {} with evaluation {}'.format(n,len(s), trial, result))
        if len(s) == 1:
            print(s[0])
            if (s[0] == self.challenge):
                return [self._colordict[s[0][i]] for i in self._slots], n
            else:
                return "Challenge {} has no solution - solver terminated after {} trials".format(self.challenge, n)
        else:
            return "Challenge {} has no solution - solver terminated after {} trials".format(self.challenge, n)

    def solver_brute_force_optimized(self):
        s = self.create_solution_generator()
        n = 0
        l = len(self._colors) ** len(self._slots)
        print('n {} and len(s) {}'.format(n,l))
        trial = ''.join(''.join('a' for _ in range(int(len(self._slots) / 2))) + ''.join('b' for _ in range(int((len(self._slots) +1)/2))))
        result = self.evaluator(trial)
        s = self.reduce_solution_set(s, trial, result)
        n += 1
        print('n {} and len(s) {} after trial {} with evaluation {}'.format(n,len(s), trial, self.evaluator(trial)))
        while len(s) > 1:
            trial = ''.join(i for i in self.create_code(s))
            result = self.evaluator(trial)
            s = self.reduce_solution_set(s, trial, result)
            n += 1
            print('n {} and len(s) {} after trial {} with evaluation {}'.format(n,len(s), trial, result))
        if len(s) == 1:
            print(''.join(i for i in s[0]))
            if (''.join(i for i in s[0]) == self.challenge):
                return [self._colordict[s[0][i]] for i in self._slots], n
            else:
                return "Challenge {} has no solution - solver terminated after {} trials".format(self.challenge, n)
        else:
            return "Challenge {} has no solution - solver terminated after {} trials".format(self.challenge, n)

    def solver_knuth(self):
        """Run Knuth's 5-guess algorithm on the given secret.
            from http://stackoverflow.com/questions/20298190/mastermind-minimax-algorithm
        """
        ALL_CODES = np.array([''.join(c) for c in self.create_solution_generator()])
        assert(self.challenge in ALL_CODES)
        codes = ALL_CODES
        key = lambda g: max(Counter(self.evaluator(g, c) for c in codes).values())
        guess = ''.join(''.join('a' for _ in range(int(len(self._slots) / 2))) + ''.join('b' for _ in range(int((len(self._slots) +1)/2))))
        n = 0
        while True:
            n += 1
            feedback = self.evaluator(guess)
            print("Guess {}: feedback {}".format(guess, feedback))
            if guess == self.challenge:
                break
            codes = self.reduce_solution_set(codes, guess, feedback)
            if len(codes) == 1:
                guess = codes[0]
            else:
                guess = min(ALL_CODES, key=key)
        return [self._colordict[guess[i]] for i in self._slots], n

    def solver_brute_generator(self):
        s = self.create_solution_generator()
        trials = []
        for triallist in s:
            trial = ''.join(i for i in triallist)
            ispossiblesolution = True
            for s in trials:
                if self.evaluator(s[0],trial) != s[1]:
                    ispossiblesolution = False
                    break
            if not ispossiblesolution:
                continue
            black, white = self.evaluator(trial)
            trials.append((trial,(black, white)))
            print('n {}th trial {} with evaluation ({}, {})'.format(len(trials), trial, black, white))
            if black == len(self._slots):
                break
        print(trials)
        print(trials[-1][0])
        print(trials[-1][1][0])
        if trials[-1][1][0] == len(self._slots):
            return [self._colordict[trial[i]] for i in self._slots], len(trials)
        else:
            return "Challenge {} has no solution - solver terminated after {} trials".format(self.challenge, len(trials))

    # def solver_by_slot(self):
    #     s = [tuple([self._colornumbers for _ in self._slots])]
    #     t=[[len(x[j]) for j in self._slots] for x in s ]
    #     s_cardinality = reduce(lambda x, y: x+y, [reduce(lambda x, y: x+y, z) for z in t])
    #     n=0
    #     print('s and cardinality of s: {} and {}'.format(s,s_cardinality))
    #     while s_cardinality > len(self._slots):
    #         n += 1
    #         trial = [s[0][i][0] for i in self._slots]
    #         s = self.reduce_by_slot(s, trial, self.evaluator(trial))
    #         t=[[len(x[j]) for j in self._slots] for x in s ]
    #         s_cardinality = reduce(lambda x, y: x+y, [reduce(lambda x, y: x+y, z) for z in t])
    #         print(s)
    #         print('n {} and cardinality of s {} after trial {} with evaluation {}'.format(n,s_cardinality, trial, self.evaluator(trial)))
    #     if s_cardinality < len(self._slots):
    #         return "Challenge {} has no solution - solver terminated after {} trials".format(self.challenge, n)
    #     else:
    #         if list(s[0]) == self.challenge:
    #             return [self._colordict[s[0][i]] for i in self._slots], n
    #         else:
    #             return "Challenge {} has no solution - solver terminated after {} trials".format(self.challenge, n)

# aux methods for solvers
    def create_solution_generator(self):
        return product(self._colorchars, repeat=len(self._slots))

    def reduce_solution_set(self,solution_set,trial,result):
        return np.array([i for i in solution_set if self.evaluator(i,trial) == result])

    # def reduce_by_slot(self, solutions_by_slot, trial, result):
    #     black, white = trial
    #     neitherblacknorwhite = len(self._slots) - black - white
    #     for i in combinations(self._slots, black):
    #
    #     if
    #
    #
    #     x= [({0},{3},{4},{2})]
    #     print('reduceresult: {}'.format(x))
    #     return x

    def binomial_coeff(n,k):
        if n<k:
            raise ValueError('k > n is not allowed in binomial_coeff(n,k).')
        if type(n) != int or type(k) != int:
            raise ValueError('binomial_coeff(n,k) is only defined for integer n and k.')
        return int(factorial(n)/(factorial(k) * factorial(n-k)))
