from random import sample, choice
from itertools import product, combinations
from functools import reduce
import numpy as np
from collections import Counter

def knuth(game):
    """Run Knuth's 5-guess algorithm on the given secret.
        adapted from http://stackoverflow.com/questions/20298190/mastermind-minimax-algorithm
        (see below for the code from stackoverflow)
    """
    ALL_CODES = np.array([''.join(c) for c in game.create_solution_generator()])
    assert(game.challenge in ALL_CODES)
    codes = ALL_CODES
    key = lambda g: max(Counter(game.evaluator(g, c) for c in codes).values())
    guess = ''.join(''.join('a' for _ in range(int(len(game._slots) / 2))) + ''.join('b' for _ in range(int((len(game._slots) +1)/2))))
    n = 0
    while True:
        n += 1
        feedback = game.evaluator(guess)
        print("Guess {}: feedback {}".format(guess, feedback))
        if guess == game.challenge:
            break
        codes = game.reduce_solution_set(codes, guess, feedback)
        if len(codes) == 1:
            guess = codes[0]
        else:
            guess = min(ALL_CODES, key=key)
    return [game.colordict[guess[i]] for i in game._slots], n



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