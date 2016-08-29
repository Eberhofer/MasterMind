import pytest
from MasterMind.game import Game
from MasterMind.solvers import knuth

@pytest.fixture
def g():
    return Game()

@pytest.fixture
def small_g():
    return Game(3,"one two three")

# @unittest.skip("********** knuth test takes too long - only run when knuth is changed **********")
def test_solution_is_correct(g):
    pytest.skip("****** THIS TEST TAKES TOO LONG - ONLY RUN WHEN WORKING ON KNUTH SOLVER *****")
    assert knuth.knuth(g)[0] == [g.colordict[g.challenge[i]] for i in g._slots]

def test_solution_is_correct_small(small_g):
    assert knuth.knuth(small_g)[0] == [small_g.colordict[small_g.challenge[i]] for i in small_g._slots]
