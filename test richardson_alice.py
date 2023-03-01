"""Imports"""
from richardson_moritz import *
from lep_csr import *
from vec_class import *

"""test richardson Bsp Tafel"""
A = csr_matrix([2, 2, 1, 2], [0, 1, 0, 1], [0, 2, 4])
b = vector([2, 2])
theta = 0.29
start_x = vector([0, 0])
maxiter = 1000000
tol = 0.00001

#Erwartung x = [0, 1]
x = richardson(A, b, start_x, theta, tol, maxiter)
print(x)

"""Test Triagonalmatrix
A = csr_matrix([2, 1, 1, 2, 1, 1, 2], [0, 1, 0, 1, 2, 1, 2], [0, 2, 5, 7])
b = vector([4, 4, 4])
theta = 0.00001
start_x = [0, 0, 0]
maxiter = 10000
tol = 0.00001

x = richardson(A, b, start_x, theta, tol, maxiter)
print(x)"""


"""Test Einheitsmatrix
A1 = csr_matrix([1, 1, 1], [0, 1, 2], [0, 1, 2, 3])
b1 = vector([0, 0, 0])
theta1 = 10e10
start_x1 = vector([0, 0, 0])
maxiter1 = 100000
tol1 = 10e15

#Erwartet x = 0
x = richardson(A1, b1, start_x1, theta1, tol1, maxiter1)
print (x)"""