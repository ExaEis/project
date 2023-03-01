"""vector class"""
class vector(list):
    def __mul__(self, scal):
        n = len(self)
        b = [0] * n
        for i in range(n):
            b[i] = self[i] * scal
        return vector(b) #, b

    def __rmul__(self, scal):
        n = len(self)
        b = [0] * n
        for i in range(n):
            b[i] = self[i] * scal
        return vector(b) #, b

    def __add__(self, vec):
        n = len(self)
        b = [0] * n
        for i in range(n):
            b[i] = self[i] + vec[i]
        return vector(b) #, b

    def __sub__(self, vec):
        n = len(self)
        b = [0] * n
        for i in range(n):
            b[i] = self[i] - vec[i]
        return vector(b) #, b

    def __norm__(self, p):
        n = len(self)
        b = [0] * n
        for i in range(n):
            b += self[i] ** p
        return b ** (1/p)

"""
#test scal_mul
vec = vector([1, 2, 3, 4])
print(vec)
"""

"""
#test vec_add
vec1 = vector([1, 2, 3])
vec2 = vector([2, 3, 4])
print(vec1-vec2)
"""

"""
norm test
r = vector([1, 2, 3, 4])
print(r.__norm__(3))
"""
