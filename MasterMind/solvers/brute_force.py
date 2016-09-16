"""
    A solver for the MasterMind game.
"""
import numpy as np

def brute_force(game):
    """
        solves MasterMind by running through generators.
        This saves memory but is dumb in the sense that it returns
        through possible solutions in lexical order.
    """
    solutions = np.array([''.join(c) for c in game.create_solution_generator()])
    i = 0
    print('i {} and ssolutions.size {}'.format(i, solutions.size))
    while solutions.size > 1:
        trial = game.create_code(solutions)
        result = game.evaluator(trial)
        solutions = np.array([c for c in game.reduce_solution_set(solutions, trial, result)])
        i += 1
        print('i {} and solutions.size {} after trial {} with ' \
                'evaluation {}'.format(i, solutions.size, trial, result))
    if solutions.size == 1:
        print(solutions[0])
        if solutions[0] == game.challenge:
            return [game.colordict[solutions[0][_]] for _ in game.get_slots()], i
        else:
            return 'Challenge {} has no solution - solver terminated ' \
                    'after {} trials'.format(game.challenge, i)
    else:
        return 'Challenge {} has no solution - solver terminated ' \
                'after {} trials'.format(game.challenge, i)
