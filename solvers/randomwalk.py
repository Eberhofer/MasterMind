from random import sample, choice
from itertools import product, combinations
from functools import reduce
import numpy as np
from collections import Counter


def solver_random_walk(self):
    trial = []
    n = 0
    while trial != self.challenge:
        trial = self.create_code()
        #print(trial)
        n += 1
    return trial, n
