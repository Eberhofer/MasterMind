from random import sample, choice
from itertools import product, combinations
from functools import reduce
from collections import Counter

def brute_force_optimized(game):
    s = game.create_solution_generator()
    n = 0
    l = len(game._colors) ** len(game._slots)
    print('n {} and len(s) {}'.format(n,l))
    trial = ''.join(''.join('a' for _ in range(int(len(game._slots) / 2))) + ''.join('b' for _ in range(int((len(game._slots) +1)/2))))
    result = game.evaluator(trial)
    s = game.reduce_solution_set(s, trial, result)
    n += 1
    print('n {} and len(s) {} after trial {} with evaluation {}'.format(n,len(s), trial, game.evaluator(trial)))
    while len(s) > 1:
        trial = ''.join(i for i in game.create_code(s))
        result = game.evaluator(trial)
        s = game.reduce_solution_set(s, trial, result)
        n += 1
        print('n {} and len(s) {} after trial {} with evaluation {}'.format(n,len(s), trial, result))
    if len(s) == 1:
        print(''.join(i for i in s[0]))
        if (''.join(i for i in s[0]) == game.challenge):
            return [game.colordict[s[0][i]] for i in game._slots], n
        else:
            return "Challenge {} has no solution - solver terminated after {} trials".format(game.challenge, n)
    else:
        return "Challenge {} has no solution - solver terminated after {} trials".format(game.challenge, n)
