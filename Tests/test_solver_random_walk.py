import pytest
from MasterMind.game import Game
from MasterMind.solvers import random_walk

@pytest.fixture
def g():
    return Game()

def test_solution_is_correct(g):
    assert random_walk.random_walk(g)[0] ==[g.colordict[g.challenge[i]] for i in g._slots]
