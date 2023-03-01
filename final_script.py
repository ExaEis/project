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

    def __norm__(self, p = 2):
        n = len(self)
        b = 0
        for i in range(n):
            b += abs(self[i]) ** p
        return b ** (1/p)

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

def richardson(A, b, start_x, theta, tol, maxiter, p = 2):
    x = start_x
    for k in range(maxiter):
        r = A.__matmul__(x) - b
        if r.__norm__() < tol:
            break
        x = x - theta * r
    return x, r.__norm__()

A = csr_matrix([1, 2, 2, 1, 1, 2, 2, 2], [0, 3, 1, 2, 3, 4, 0, 2], [0, 2, 4, 5, 6, 8])
b = vector([1, 2, 0, 1, 1])
start_x = vector([0, 0, 0, 0, 0])
theta = 0.000000001
tol = 0.000000000001
maxiter = 10000

x = richardson(A, b, start_x, theta, tol, maxiter)
print(x)