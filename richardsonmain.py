"""File für relax. Richardson-Hauptrechnung"""
from csr_matrix import csr_matrix
from vec_class import vector
a = csr_matrix ([1,2,2,1,1,2,2,2],[0,3,1,2,3,4,0,2],[0,3,5,6,7,9])
#insert matrix as csr matrix
maxiter = 55
#insert number of iterations
startvalue = vector ([0,0,0,0,0])
#choose vector to start from
x = startvalue
b = vector ([1,2,0,1,1])
#insert target vector
h = 0.1
#insert scaling
tol = 0.5
#insert toleration

for k in range (maxiter):
    r = a@x-b
    if vector.__norm__(r) < tol:
        print(x)
        break
    x = x-h*r
