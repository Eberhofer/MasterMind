from random import sample, choice
from itertools import product, combinations
from functools import reduce
import numpy as np
from collections import Counter

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



# def knuth(secret):
#     """Run Knuth's 5-guess algorithm on the given secret.
#         from http://stackoverflow.com/questions/20298190/mastermind-minimax-algorithm
#     """
#     ALL_CODES
#     assert(secret in ALL_CODES)
#     codes = ALL_CODES
#     key = lambda g: max(Counter(evaluate(g, c) for c in codes).values())
#     guess = 'AABB'
#     while True:
#         feedback = evaluate(guess, secret)
#         print("Guess {}: feedback {}".format(guess, feedback))
#         if guess == secret:
#             break
#         codes = [c for c in codes if evaluate(guess, c) == feedback]
#         if len(codes) == 1:
#             guess = codes[0]
#         else:
#             guess = min(ALL_CODES, key=key)
