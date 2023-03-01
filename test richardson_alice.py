"""Imports"""
from richardson_moritz import *
from lep_csr import *
from vec_class import *

"""test richardson Bsp Tafel"""
A = csr_matrix([(1, 0, 0, 0, 2), (0, 2, 0, 0, 0), (0, 1, 0, 0, 2), (2, 0, 1, 0, 0), (0, 0, 0, 2, 0)], [0, 3, 1, 2, 3, 4, 0, 2], [0, 2, 4, 5, 6, 8])
b = vector ([(1, 2, 0, 1, 1)])
p = 2
theta = 0.000001
x = vector([0, 0, 0, 0, 0])
maxiter = 100000
tolerance = 0.00001

#x = richardson(A,b,theta,x,maxiter, tolerance, p)
#print (x)

"""Test Einheitsmatrix"""
A1 = csr_matrix([(1, 0, 0), (0, 1, 0), (0, 0, 1)], [0, 1, 2], [0, 1, 2, 3])
b1 = vector ([0, 0, 0])
p1 = 2
theta1 = 0.000001
x1 = vector ([0, 0, 0])
maxiter1 = 100000
tolerance1 = 0.00000001

#Erwartet x = 0
x = richardson(A1, b1, theta1, x1, maxiter1, tolerance1, p1)
print (x)