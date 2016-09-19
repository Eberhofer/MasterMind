.. _api:

API Documentation
=================

The game class
--------------

Apart from a little helper function :func:`binomial_coeff.binomial_coeff` in
it's own module, the main code is in :class:`game.Game`. This class uses a set
of `constants`_.

.. automodule:: game
    :members:

.. automodule:: binomial_coeff
    :members:

.. _api_solvers:

Solvers
-------

.. automodule:: solvers.knuth
    :members:

.. automodule:: solvers.brute_force
    :members:

.. automodule:: solvers.brute_force_optimized
    :members:

.. automodule:: solvers.brute_force_generator
    :members:

.. automodule:: solvers.generator
    :members:

.. automodule:: solvers.random_walk
    :members:

.. automodule:: solvers.knuth2
    :members:

.. _constants:

Constants
---------
:class:`game.Game` uses the literal string 'abcdefghijklmnopqrstuvwxyz' as
potential keys for the :meth:`game.Game.colordict` for translating the codes
back to colors.
