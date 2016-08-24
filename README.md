# MasterMind

# Intro
A project to explore MasterMind solution strategies. It already uses numpy, although at this stage, there is no measurable performance benefit over python lists - numpy is not essential and I may decide to throw it out again.

## Games
The code creates a game from the Game class in the top level of the hierarchy. It can be used as follows:

from game import Game

Games can then be created using a simple constructor call with the number of slots and the colors (as a space separated string). In the following, g is a classic MasterMind with 6 colors and 4 slots while h is a more exotic game with 5 slots and characters from OnePiece as colors. Please note that fancy colors are possible, but that they are represented as the first n lower case characters where n is the number of different colors. For h, n is 8.

```
g=Game()
h=Game(slots=5,colors='Ruffy Nami Sanji Zorro Robin Frankie Lysop Trafalgar')
```

##playing MasterMind
The games can be played by giving codes to the games evaluator, which returns a tuple of 2 integers representing the black and white knobs respectively. Two examples:

```
in: g.evaluator('abcd')
out: (0,2)
in: h.evaluator('abcde')
out: (2,2)
```

For a new challenge code, use g.set_challenge().

## solvers
The more interesting aspect of the code is the set of algorithms to solve games. A number of solvers are provided and can be imported from the solvers folder:

```
from solvers.knuth import knuth
from solvers.brute_force import brute_force
```

The solvers can then be applied to a game as follows:


```
knuth(g)
brute_force(h)
```

While MasterMind is probably **the** game for the beginning programmer and the literature on it is abundant, it is surprisingly difficult to come up with a canonical solver that scales well. Further, there are different notions of 'optimal'. knuth, for example, never needs more than 5 attempts for the classic MasterMind game. However, it's o(n2) and starts to fail quickly if the number of slots and/or colors is increased. In addition, generalizing the starting point ('aabb') is not trivial. brute_force, on the other hand, is very quick, gets the result usually in 5 guesses or less and scales reasonably well being o(n). However, it is very memory intensive and can take more than 5 guesses (I don't know what the worst case is) to arrive at the solution. brute_force_generator takes care of the memory issue, but in its current implementation (lexical order) frequently requires 9 or 10 guesses.

## create your own solvers
The game class offers some helper methods to facilitate the creation of new solvers. That was the point of the project to begin with. The methods are (assuming a game g already constructed):

### g.create_code(optional solution_set)
If called without arguments, this returns a random code for the game g. If a solution_set is given, the method chooses and returns a random element of that set. (Technically, it treats the solutionset as a list).

### g.create_solution_generator()
This method returns a generator yielding all possible solutions as lists. This is a generator, which can be easily turned into a list of solutions as follows:

```
[''.join(solution) for solution in g.create_solution_generator]
```

Note that the current implementation ofd the generator yields lists and the codes are just strings. "'.join(list)'" creates a string from each list.

### g.reduce_solution_set(solution_set,guess,feedback)
This method returns a numpy array  of possible solutions that remain in a given solution_set after guess received feedback. The method is essentially a comprehension calling g.evaluator for each element of solution_set.
