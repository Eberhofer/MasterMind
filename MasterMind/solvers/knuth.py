"""
    Knuth's algorithm (simplified)
    ------------------------------
"""
from collections import Counter
import numpy as np


def knuth(game):
    """Run Knuth's 5-guess algorithm on the given secret.
        adapted from
        http://stackoverflow.com/questions/20298190/mastermind-minimax-algorithm
        (see below for the code from stackoverflow)

        The code is simplified in the way it treats ties in the minmax function.
        Instead of going to the next level to resolve ties, we simply take the
        first code that fulfills the minmax condition.

        Returns the solution translated back into the game colors.
    """
    solutions = game.create_solution_generator()
    _all_codes = np.array([''.join(_) for _ in solutions])
    codes = _all_codes
    key = lambda g: max(Counter(game.evaluator(g, _) for _ in codes).values())
    n_slots = len(game.slots)
    guess = ''.join(''.join('a' for _ in range(int(n_slots / 2))) +
                    ''.join('b' for _ in range(int((n_slots +1)/2))))
    i = 0
    while True:
        i += 1
        feedback = game.evaluator(guess)
        print("Guess {}: feedback {}".format(guess, feedback))
        if guess == game.challenge:
            break
        codes = np.array([c for c in game.reduce_solution_set(codes, guess, feedback)])
        if len([_ for _ in codes]) == 1:
            guess = codes[0]
        else:
            # score = np.array([max(Counter(game.evaluator(g, c) for c in codes).values())
            #             for g in ALL_CODES])
            guess = min(_all_codes, key=key)
    return [game.colordict[guess[_]] for _ in game.slots], i



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
