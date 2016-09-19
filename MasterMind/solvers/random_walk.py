"""
    Random walk
    -----------
"""

def random_walk(game):
    """
        Solves MasterMind by throwing out random codes.
        On average takes about 5 time n guesses, where n
        is the number of possible solutions of the Mastermind Game.
        For 6\ :sup:`4`, this means about 6000 guesses.

        Returns the solution translated back into the game colors.
    """
    trial = []
    i = 0
    while trial != game.challenge:
        trial = game.create_code()
        #print(trial)
        i += 1
    return  [game.colordict[trial[_]] for _ in game.slots], i
