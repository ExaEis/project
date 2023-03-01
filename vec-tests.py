#Test Vektor-Klassen

from vec_class import *
def test_mul():
    assert vector([1, 2, 3, 4])*3 == vector([3, 6, 9, 12])
    assert vector([1, 1, 1, 3])*2 != vector([2, 1, 2, 6])
    assert vector([1, 2, 3, 4])*0 != vector([0])
    assert vector([3, 3, 3])*(1/3) == vector([1, 1, 1])
    assert vector([0, 0, 0, 0])*4 == vector([0, 0, 0, 0])
test_mul()


def test_rmul():
    assert 3*vector([1, 2, 3, 4]) == vector([3, 6, 9, 12])
    assert 2*vector([1, 1, 1, 3]) != vector([2, 1, 2, 6])
    assert 0*vector([1, 2, 3, 4]) == vector([0, 0, 0, 0])
    assert (1/3)*vector([9, 9, 9]) == vector([3, 3, 3])
    assert 11*vector([0, 0, 0, 0]) == vector([0, 0, 0, 0])
test_rmul()

def test_add():
    assert vector([1, 2, 3]) + vector ([0, 1, 2]) == vector([1, 3, 5])
    assert vector([6]) + vector([3]) == vector([9])
    assert vector([0, 0, 0]) + vector([1, 2, 3]) == vector([1, 2, 3])
    assert vector([3, 3, 1]) + vector([1, 2, 1]) != vector([3, 3, 5])
    assert vector([-5, 3]) + vector([3, -2]) == vector([-2, 1])
test_add()

def test__sub__():
    assert vector([1, 1, 1]) == vector([1, 2, 3]) - vector([0, 1, 2])
    assert vector([1, 2]) == vector([2, 4]) - vector([1, 2])
    assert vector([1, 3, 5, 3, 1]) == vector([3, 5, 7, 5, 3]) - vector([2, 2, 2, 2, 2])
    assert vector([2, 3, 5, 1]) == vector([5, 4, 8, 7]) - vector([3, 1, 3, 6])
    assert vector([6]) == vector([9]) - vector([3])
test__sub__()

def test_norm():
    assert vector([3, 4]).__norm__() == 5
    assert vector([1, 2, 3]).__norm__(3) != 3
    assert vector([0, 0, 0]).__norm__(8) == 0
    assert vector([1, 1, 1, 1, 1, 1, 1, 1]).__norm__(3) == 2
    assert vector([3, 3]).__norm__(1) == 6
test_norm()

