import pytest
from MasterMind.game import Game
from MasterMind.solvers import brute_force

@pytest.fixture
def g():
    return Game()

def test_solution_is_correct(g):
    assert brute_force.brute_force(g)[0] == [g.colordict[g.challenge[i]] for i in g._slots]
