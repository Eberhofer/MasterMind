.. MasterMind documentation master file, created by
   sphinx-quickstart on Fri Sep 16 17:12:17 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MasterMind's documentation!
======================================

A project to explore n\ :sup:`m` MasterMind `solution strategies`_, where m is
the number of slots and n is the number of colors. The 6\ :sup:`4` MasterMind is
the classic game. In the current state, the project only explores interactive
strategies, but the code is prepared to handle static solutions as well and
should support solution strategies for generic n and m.

Note on the dependencies: The game module uses the standard library only.
However, some of the solvers use numpy, although at this stage, there is no
measurable performance benefit over python lists - numpy is not essential and
I may decide to throw it out again. Other than that, just the standard library.
Oh, and it's Python 3.5.2 but it should really work for any Python 3 environment.

This project is an exploration into solving strategies for MasterMind.
It's core is the :class:`game.Game` class, which defines a n\ :sup:`m` Mastermind game
with m slots and n colors and provides certain methods to assist writing
solution strategies.

Simple use
----------
For the impatient: here's a quick overview of how to use this project. Normally,
all you have to do is import and run, like this::

    from MasterMind.game import Game
    g=Game()
    h=Game(slots=5,colors='Ruffy Nami Sanji Zorro Robin Frankie Lysop Trafalgar')

This will generate a 6\ :sup:`4` game g and a 8\ :sup:`5` game h with a challenge
code each and with the corresponding methods and properties.

For more information about how to use this library, see the :ref:`api`.

How it works
------------
MasterMind is essentially a finite code breaking game and each strategy needs
to know the game's properties and an evaluator plus some convenience methods and
properties to generate solutions or translate codes to colors.
The game can be played on the console::

    in: g.evaluator('abcd')
    out: (0,2)
    in: h.evaluator('abcde')
    out: (2,2)

Solution strategies
-------------------
The folder :ref:`solvers <api_solvers>` contains a number of strategies to solve
MasterMind. It's actually an invitation to improve upon them and to suggest or
try new strategies. My goal was to be general both in the :class:`game.Game`
class and in the :ref:`solvers <api_solvers>`. Each :ref:`solver <api_solvers>` takes an instantiated
game as argument and finds the solution for it. :ref:`Solvers <api_solvers>` can also be written for
what's known as static MasterMind. In static MasterMind, the codebreaker tries
to provide (in one go) a set of guesses that, together with the evaluations,
will allow her to break the code in the next guess.

Literature
----------
There is a lot of literature on the game and I only want to present some pointers:
Wikipedia has a great entry for MasterMind:
`Mastermind (board game) <https://en.wikipedia.org/wiki/Mastermind_(board_game)>`_.
This paper provides a good overview over the scholarly literature:
`Playing Mastermind with Many Colors <http://people.mpi-inf.mpg.de/~winzen/Mastermind.pdf>`_.

Tests
-----
There are doctests and unit tests written in pytests to cover most of the
:class:`game.Game` class and some :ref:`solvers <api_solvers>`. Tests are not
comprehensive, though.



Contents:

.. toctree::
   :maxdepth: 2

   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
