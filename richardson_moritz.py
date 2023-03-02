from vec_class import *
from csr_matrix import *
def richardson(A, b, start_x, theta, tol, maxiter, p = 2):
    x = start_x
    for k in range(maxiter):
        r = A.__matmul__(x) - b
        if r.__norm__() < tol:
            break
        x = x - theta * r
    return x, r.__norm__(), k


A = csr_matrix(([4,3,1,4,3,1,4], [0,1,0,1,2,1,2], [0,2,5,7]))
b = vector([2,2,2]) #wähle theta = 1/b+root(2ac)
start_x = vector([0, 0, 0])
theta = 0.15505
tol = 0.001
maxiter = 10000

x = richardson(A, b, start_x, theta, tol, maxiter)
print(x)