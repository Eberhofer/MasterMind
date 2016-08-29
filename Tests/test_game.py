import pytest
from MasterMind.game import Game
from MasterMind.solvers import random_walk

@pytest.fixture
def g():
    return Game()

def test_colors(g):
    assert g._colors == set(['blue', 'green', 'yellow', 'orange', 'red', 'brown'])

def test_slots(g):
    assert g._slots == range(4)

def test_init(g):
    for i in g._slots:
        assert g.challenge[i] in g._colorchars

def test_challenge_evaluates_correctly(g):
    assert g.evaluator(g.challenge) == (4,0)

def test_benchmark_evaluates_(g):
    assert g.evaluator([1,2,3,4], [1,3,6,2]) == (1,2)

def test_len_solution_generator(g):
    s = [i for i in g.create_solution_generator()]
    assert len(s) == len(g._colors) ** len(g._slots)
