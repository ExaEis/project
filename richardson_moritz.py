from vec_class import *
from lep_csr import *
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