from vec_class import *
class csr_matrix:
    def __init__(self, data, indices, indptr):
        self.data = data
        self.indices = indices
        self.indptr = indptr

    def __matmul__(self, x):
        m = len(self.indptr) - 1
        b = [0] * m
        for i in range(m):
            intervall = self.indptr[i:i + 2]
            for j in range(intervall[0], intervall[1]):
                b[i] = b[i] + self.data[j] * x[self.indices[j]]
        return vector(b)

