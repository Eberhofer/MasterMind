# MasterMind

# Intro
A project to explore n<sup>m</sup> MasterMind solution strategies, where m is the number of slots and n is the number of colors. 6<sup>4</sup> MasterMind is the classic game. In the current state, the project only explores interactive strategies, but the code is prepared to handle static solutions as well and should support solution strategies for generic n and m.

Note on the dependencies: The game module uses the standard library only. However, some of the solvers use numpy, although at this stage, there is no measurable performance benefit over python lists - numpy is not essential and I may decide to throw it out again. Other than that, just the standard library. Oh, and it's Python 3.5.2 but it should really work for any python 3 environment.

## Games
The code creates a game from the Game class in the top level of the hierarchy. It can be used as follows:

```
from MasterMind.game import Game
```

Games can then be created using a simple constructor call with the number of slots and the colors (as a space separated string). In the following, g is a classic (4,6) MasterMind with 6 colors and 4 slots while h is a more exotic (5,8) game with 5 slots and 8 characters from OnePiece as colors. Please note that fancy colors are possible, but that they are represented as the first n lower case characters where n is the number of different colors. The solvers do return the solution in the colors given using g.colordict.

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
from MasterMind.solvers.knuth import knuth
from MasterMind.solvers.brute_force import brute_force
from MasterMind.solvers.brute_force_optimized import brute_force_optimized as bfo
```

The solvers can then be applied to a game as follows:

```
knuth(g)
brute_force(h)
bfo(h)
```

While MasterMind is a very popular game for the beginning programmer and the literature on it is abundant, it is surprisingly difficult to come up with a canonical solver that scales well. Further, there does not appear to be one single best algortihm. Rather, there are different notions of 'optimal' dependent on preference. knuth, for example, never needs more than 5 attempts for the classic MasterMind game and is optimal from a worst case perspective. However, execution time explodes quickly with O(n<sup>2</sup>) if the number of slots and/or colors is increased. In addition, generalizing the starting point ('aabb') is not trivial. brute_force, on the other hand, is very quick, gets the result usually in 5 guesses or less and scales reasonably well being O(n). However, it is memory intensive and can take more than 5 guesses to arrive at the solution. brute_force_generator takes care of the memory issue, is about as fast brute_force on average, but in its current implementation (lexical order) frequently requires 9 or 10 guesses. brute_force_optimized alleviates the memory issue somewhat (by using a generator initially instead of a list) and appears to be optimal from a practical point of view. For example, it can solve 6-color MasterMind with 10 slots on a raspberry pi 3  in roughly two hours, while brute_force does not have enough memory for 9 slots and knuth already requires >20 minutes for 5 slots.
Apparently, Chvátal found in a scholarly paper written in 1983 that throwing random guesses from the set of possible solutions (like the 'brute_force' solver does) is quite optimal for a large range of games. :-) 

## create your own solvers
The game class offers some methods to facilitate the creation of new solvers. That was the point of the project to begin with. The methods are (assuming a game g already constructed):

### g.create_code(optional solution_set)
If called without arguments, this returns a random code for the game g. If a solution_set is given, the method chooses and returns a random element of that set. (Technically, it treats the solutionset as a list).

### g.create_solution_generator()
This method returns a generator yielding all possible solutions as lists. This is a generator, which can be easily turned into a list of solutions as follows:

```
[''.join(solution) for solution in g.create_solution_generator]
```

Note that the current implementation of the generator yields lists and the codes are just strings. "'.join(list)'" creates a string from each list.

### g.reduce_solution_set(solution_set,guess,feedback)
This method returns a numpy array  of possible solutions that remain in a given solution_set after guess received feedback. The method is essentially a comprehension calling g.evaluator for each element of solution_set.

### g.colordict
This is not a method but a python dictionary translating the letters into colors. It can be used to return a list of colors from the solver instead of a string of lower case letters

# Links

## General / studies
https://en.wikipedia.org/wiki/Mastermind_(board_game) (accessible introduction with good overview over algorithms)
http://people.mpi-inf.mpg.de/~winzen/Mastermind.pdf (a nice scholarly overview over the literature and theory)
http://mathworld.wolfram.com/Mastermind.html
https://arxiv.org/pdf/1305.1010.pdf
http://www.philos.rug.nl/~barteld/master.pdf

## Implementations
http://www.stoyanr.com/2012/09/masterminder-java-library-of-mastermind.html

## Microimplementations
https://mail.python.org/pipermail/python-list/2002-August/126236.html
http://www.mystrobl.de/ws/pic/mm47/index.htm
http://www.mystrobl.de/ws/pic/mm47/mm47bas.htm
