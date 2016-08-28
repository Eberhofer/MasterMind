from random import sample, choice
from itertools import product, combinations
from functools import reduce
import numpy as np
from collections import Counter


def random_walk(game):
    trial = []
    n = 0
    while trial != game.challenge:
        trial = game.create_code()
        #print(trial)
        n += 1
    return  [game.colordict[trial[i]] for i in game._slots], n
