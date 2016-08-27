from random import sample, choice
from itertools import product, combinations
from functools import reduce
import numpy as np
from collections import Counter

def brute_force(game):
    s = np.array([''.join(c) for c in game.create_solution_generator()])
    n = 0
    print('n {} and len(s) {}'.format(n,len(s)))
    while len(s) > 1:
        trial = game.create_code(s)
        result = game.evaluator(trial)
        s = game.reduce_solution_set(s, trial, result)
        n += 1
        print('n {} and len(s) {} after trial {} with evaluation {}'.format(n,len(s), trial, result))
    if len(s) == 1:
        print(s[0])
        if (s[0] == game.challenge):
            return [game.colordict[s[0][i]] for i in game._slots], n
        else:
            return "Challenge {} has no solution - solver terminated after {} trials".format(game.challenge, n)
    else:
        return "Challenge {} has no solution - solver terminated after {} trials".format(game.challenge, n)
