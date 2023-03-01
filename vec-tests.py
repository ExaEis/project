#Test Vektor-Klassen

from vec_class import *
def test_mul():
    assert vector([1, 2, 3, 4])*3 == vector([3, 6, 9, 12])
    assert vector([1, 1, 1, 3])*2 != vector([2, 1, 2, 6])
    assert vector([1, 2, 3, 4])*0 == vector([0])
    assert vector([3, 3, 3])*(1/3) == vector([1, 1, 1])
    assert vector([0, 0, 0, 0])*4 == vector([0])


def test_rmul():
    assert 3*vector([1, 2, 3, 4]) == vector([3, 6, 9, 12])
    assert 2*vector([1, 1, 1, 3]) != vector([2, 1, 2, 6])
    assert vector([1, 2, 3, 4]) * 0 == vector([0])
    assert vector (1/3)*([9, 9, 9]) == vector([3, 3, 3])
    assert vector 11*([0, 0, 0, 0]) == vector([0])


