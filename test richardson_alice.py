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
tol = 0.0001

#Erwartung x = [0, 1]
#x = richardson(A, b, start_x, theta, tol, maxiter)
#print(x)

"""Test Triagonalmatrix """
A2 = csr_matrix([2, 2, 2], [0, 1, 2], [0, 1, 2, 3])
b2 = vector([4, 4, 4])
theta2 = 0.29
start_x2 = vector([0, 0, 0])
maxiter2 = 10000
tol2 = 0.00001

#Erwartung x = [2, 2, 2]
#x = richardson(A2, b2, start_x2, theta2, tol2, maxiter2)
#print(x)


"""Test Einheitsmatrix"""
A1 = csr_matrix([1, 1, 1], [0, 1, 2], [0, 1, 2, 3])
b1 = vector([0, 0, 0])
theta1 = 10e10
start_x1 = vector([0, 0, 0])
maxiter1 = 100000
tol1 = 10e15

#Erwartet x = 0
#x = richardson(A1, b1, start_x1, theta1, tol1, maxiter1)
#print (x)