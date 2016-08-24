# MasterMind

##Games
The code creates a game from the Game class in the top level of the hierarchy. It can be used as follows:

from game import Game

Games can then be created using a simple constructor call with the number of slots and the colors (as a space separated string). In the following, g is a classic MasterMind with 6 colors and 4 slots while h is a more exotic game with 5 slots and characters from OnePiece as colors. Please note that fancy colors are possible, but that they are represented as the first n lower case characters where n is the number of different colors. For h, n is 8.

g=Game()
h=Game(slots=5,colors='Ruffy Nami Sanji Zorro Robin Frankie Lysop Trafalgar')

The games can be played by giving codes to the games evaluator, which returns a tuple of 2 integers representing the black and white knobs respectively. Two examples:

in: g.evaluator('abcd')
out: (0,2)
in: h.evaluator('abcde')
out: (2,2)

## solvers
The more interesting aspect of the code is the set of algorithms to solve games. A number of solvers are provided and can be imported from the solvers folder:

from solvers.knuth import knuth
from solvers.brute_force import brute_force

The solvers can then be applied to a game as follows:
knuth(g)
brute_force(h)

While MasterMind is probably the game for the beginning programmer and the literature on it is abundant, it is surprisingly difficult to come up with a canonical solver that scales well. Further, there are different notions of 'optimal'. knuth, for example, never needs more than 5 attempts for the classic MasterMind game. However, it's o(n2) and starts to fail quickly if the number of slots and/or colors is increased. In addition, generalizing the starting point ('aabb') is not trivial. brute_force, on the other hand, is very quick, gets the result usually in 5 guesses or less and scales reasonably well being o(n). However, it is very memory intensive and can take more than 5 guesses (I don't know what the worst case is) to arrive at the solution. brute_force_generator takes care of the memory issue, but in its current implementation (lexical order) frequently requires 9 or 10 guesses. 
