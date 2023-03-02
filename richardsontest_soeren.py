from lep_csr import csr_matrix
from vec_class import vector

"""

"""
A = csr_matrix ([0.5,0.3,0.4,0.1,0.75],[0,1,2,3,4],[0,1,2,3,4,5])
b = vector ([3,4,2,5,6])
x = vector ([1,1,1,1,1])
tol = 0.00001
maxiter = 100000
h = 0.001
def richardson(A, b, x, tol, maxiter, h):

    for k in range (maxiter):
        r = A@x-b
        if vector.__norm__(r) < tol:
            print("finished in range")
            break
        x = x-h*r
    print(x)

richardson(A, b, x, tol, maxiter, h)



"""
for csr matrix A: ([10,-2,3,9,7,8,7,3,8,7,5,8,9,13],[0,4,0,1,1,2,3,,0,2,3,4,1,3,4],[0,2,4,7,11,14])
target vector ([12,3,5,7,2]) and 
startvector ([1,1,1,1,1])
"""
A = csr_matrix ([10,-2,3,9,7,8,7,3,8,7,5,8,9,13],[0,4,0,1,1,2,3,0,2,3,4,1,3,4],[0,2,4,7,11,14])
b = vector ([12,3,5,7,2])
x = vector ([1,1,1,1,1])
tol = 0.0001
maxiter = 150000
h = 0.0001
def richardsontest(A, b, x, tol, maxiter, h):
    for k in range (maxiter):
        r = A @ x - b
        if vector.__norm__(r) < tol:
            print("finished in range")
            break
        x = x - h * r
    print(x)
    expected = vector ([103/91, -4/91, 1/234, 617/819, -31/91])
    t = x - expected
    if vector.__norm__(t) < 0.001:
        print ("solution is correct")
    else:
        print ("solution is false")
    print (expected)

richardsontest( A, b, x, tol, maxiter, h)

"""
ich denke, das der Test in der Theorie funktionieren würde, man aber, ab einem bestimmten Iterations-Schrittweiten-verhältnis,
in einen Zahlenraum reinkomme, in dem die Operationen nicht mehr definiert sind.
"""