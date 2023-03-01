"sub_test"

from vec_class import *

def test__sub__():
    assert vector([1, 1, 1]) == vector([1, 2, 3]) - vector ([0, 1, 2])
    assert vector([1, 2]) == vector([2, 4]) - vector([1, 2])
    assert vector([1, 3, 5, 3, 1]) == vector([3, 5, 7, 5, 3]) - vector([2, 2, 2, 2, 2,])
    assert vector([2, 3, 5, 1]) == vector([5, 4, 8, 7]) - vector([3, 1, 3, 6])
    assert vector([6]) == vector([9]) - vector([3])
test__sub__()
