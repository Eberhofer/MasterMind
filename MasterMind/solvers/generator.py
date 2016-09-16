"""
    A solver for the MasterMind game.
"""
def generator(game):
    """
        solves MasterMind by running through generators.
        This saves memory but is dumb in the sense that it returns
        through possible solutions in lexical order.
    """
    solution_generator = game.create_solution_generator()
    trial = game.create_code()
    trials = [(trial, game.evaluator(trial))]
    for triallist in solution_generator:
        trial = ''.join(i for i in triallist)
        ispossiblesolution = True
        for tenttrial in trials:
            if game.evaluator(tenttrial[0], trial) != tenttrial[1]:
                ispossiblesolution = False
                break
        if not ispossiblesolution:
            continue
        black, white = game.evaluator(trial)
        trials.append((trial, (black, white)))
        print('n {}th trial {} with evaluation' \
                '({}, {})'.format(len(trials), trial, black, white))
        if black == len(game.get_slots()):
            break
    print(trials)
    print(trials[-1][0])
    print(trials[-1][1][0])
    if trials[-1][1][0] == len(game.get_slots()):
        return [game.colordict[trial[i]] for i in game.get_slots()], len(trials)
    else:
        return "Challenge {} has no solution - solver terminated ' \
                'after {} trials".format(game.challenge, len(trials))
