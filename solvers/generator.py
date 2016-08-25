from random import sample, choice
from itertools import product, combinations
from functools import reduce
import numpy as np
from collections import Counter

def generator(game):
    s = game.create_solution_generator()
    trial = game.create_code()
    trials = [(trial, game.evaluator(trial))]
    for triallist in s:
        trial = ''.join(i for i in triallist)
        ispossiblesolution = True
        for s in trials:
            if game.evaluator(s[0],trial) != s[1]:
                ispossiblesolution = False
                break
        if not ispossiblesolution:
            continue
        black, white = game.evaluator(trial)
        trials.append((trial,(black, white)))
        print('n {}th trial {} with evaluation ({}, {})'.format(len(trials), trial, black, white))
        if black == len(game._slots):
            break
    print(trials)
    print(trials[-1][0])
    print(trials[-1][1][0])
    if trials[-1][1][0] == len(game._slots):
        return [game.colordict[trial[i]] for i in game._slots], len(trials)
    else:
        return "Challenge {} has no solution - solver terminated after {} trials".format(game.challenge, len(trials))
