"""
    Brute force optimized
    ---------------------
"""

def brute_force_optimized(game):
    """
        Solves MasterMind by running through generators.
        This saves memory but is dumb in the sense that it returns
        through possible solutions in lexical order.
        Returns the solution translated back into the game colors.
    """
    solutions = game.create_solution_generator()
    i = 0
    n_solutions = len(game.colordict) ** len(game.slots)
    print('i {} and len(solutions) {}'.format(i, n_solutions))
    n_slots = len(game.slots)
    trial_inner = ''.join('a' for _ in range(int(n_slots / 2)))
    trial_inner += ''.join('b' for _ in range(int((n_slots + 1) / 2)))
    trial = ''.join(trial_inner)
    result = game.evaluator(trial)
    solutions = [c for c in game.reduce_solution_set(solutions, trial, result)]
    i += 1
    print('n {} and len(s) {} after trial {} with evaluation {}' \
            ''.format(i, len(solutions), trial, game.evaluator(trial)))
    while len(solutions) > 1:
        trial = ''.join(i for i in game.create_code(solutions))
        result = game.evaluator(trial)
        solutions = [c for c in
                     game.reduce_solution_set(solutions, trial, result)]
        i += 1
        print('n {} and len(s) {} after trial {} with evaluation {}' \
                ''.format(i, len(solutions), trial, result))
    if len(solutions) == 1:
        print(''.join(_ for _ in solutions[0]))
        if ''.join(_ for _ in solutions[0]) == game.challenge:
            return [game.colordict[solutions[0][i]]
                    for i in game.slots], i
        else:
            return 'Challenge {} has no solution - solver terminated ' \
                    'after {} trials'.format(game.challenge, i)
    else:
        return 'Challenge {}) has no solution - solver terminated ' \
                'after {} trials'.format(game.challenge, i)
