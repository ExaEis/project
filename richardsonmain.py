"""File für relax. Richardson-Hauptrechnung"""
from lep_csr import csr_matrix
from vec_class import vector

a = csr_matrix ([0.5,0.3,0.4,0.1,0.75],[0,1,2,3,4],[0,1,2,3,4,5])
#insert matrix as csr matrix
maxiter = 100000
#insert number of iterations
startvalue = vector ([1,1,1,1,1])
#choose vector to start from
x = startvalue
b = vector ([3,4,2,5,6])
#insert target vector
h = 0.001
#insert scaling
tol = 0.00001
#insert toleration

for k in range (maxiter):
    r = a@x-b
    if vector.__norm__(r) < tol:
        print ("finished in ranged")
        break
    x = x-h*r
print(x)