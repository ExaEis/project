"""vector class"""
class vector(list):
    def __init__(self, tupel):
        self.tupel = tupel
        self.len = len(self.tupel)

    def __mul__(self, scal):
        b = [0] * self.len
        for i in range(self.len):
            b[i] = self.tupel[i] * scal
        return vector(b) #, b

    def __rmul__(self, scal):
        b = [0] * self.len
        for i in range(self.len):
            b[i] = self.tupel[i] * scal
        return vector(b) #, b

    def __add__(self, vec):
        b = [0] * self.len
        for i in range(self.len):
            b[i] = self.tupel[i] + vec.tupel[i]
        return vector(b) #, b

    def __sub__(self, vec):
        b = [0] * self.len
        for i in range(self.len):
            b[i] = self.tupel[i] - vec.tupel[i]
        return vector(b) #, b

    def __norm__(self, p):
        b = 0
        for i in range(self.len):
            b += self.tupel[i] ** p
        d = b ** (1/p)
        return d

"""
test scal_mul
vec = vector([1, 2, 3, 4])
print(vec*4)
"""

"""
test vec_add
vec1 = vector([1, 2, 3])
vec2 = vector([2, 3, 4])
print(vec1-vec2)
"""

"""
norm test
r = vector([1, 2, 3, 4])
print(r.__norm__(3))
"""
