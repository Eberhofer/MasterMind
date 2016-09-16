"""
    A solver for the MasterMind game.
"""

def brute_force_generator(game):
    """
        solves MasterMind by running through generators.
        This saves memory but is dumb in the sense that it returns
        through possible solutions in lexical order.
    """
    solutions = game.create_solution_generator()
    trials = []
    for triallist in solutions:
        trial = ''.join(i for i in triallist)
        ispossiblesolution = True
        for tent_trial in trials:
            if game.evaluator(tent_trial[0], trial) != tent_trial[1]:
                ispossiblesolution = False
                break
        if not ispossiblesolution:
            continue
        black, white = game.evaluator(trial)
        trials.append((trial, (black, white)))
        print('{}th trial {} with evaluation ({}, {})' \
                ''.format(len(trials), trial, black, white))
        if black == len(game.get_slots()):
            break
    print(trials)
    print(trials[-1][0])
    print(trials[-1][1][0])
    if trials[-1][1][0] == len(game.get_slots()):
        return [game.colordict[trial[_]] for _ in game.get_slots()], len(trials)
    else:
        return "Challenge {} has no solution - solver terminated after {} ' \
                'trials".format(game.challenge, len(trials))
