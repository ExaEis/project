from vec_class import *
from csr_matrix import *

def richardson_verfahren (A,b,x,theta,maxiter,tol):
    matrix_a = csr_matrix(A)
    vec_b = vector(b)
    vec_x = vector(x)
    r_k = 0
    r_k_liste = []

    for k in range(maxiter):
        r_k = (matrix_a @ vec_x) - b
        r_k_liste.append(r_k.__norm__())
        if r_k.__norm__() < tol:
            break
        vec_x = vec_x - (theta * r_k)

    return vec_x, k, r_k.__norm__(), #r_k_liste