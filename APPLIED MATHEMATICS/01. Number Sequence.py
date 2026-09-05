# ----------- 01. NUMBER SEQUENCE -----------
# IMPORTING THE PACKAGES
# THIS CELL NEEDS TO BE EXECUTED BEFORE THEY CAN BE USED
import math
import numpy as np
import scipy as sp
import sympy as sy
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import hashlib
import cryptography
# %matplotlib inline
# ===================================================================================

# Creating symbolic variable n (which is now an integer)
n = sy.symbols('n', integer=True)
# -----------------------------------------------------------------------------------
# a) ARITHMETIC SEQUENCE:------------------------------------------------------------
# -----------------------------------------------------------------------------------
# General term a_n with (a_1 = 7; d = 4):
a_n = 4*n+3
print('- General Term of Arithmetic Sequence (with a1=7 and d=4): a_n = ', a_n)

# Calculating the member a_45 with subs-method:
a_45 = a_n.subs(n, 45)
print('- Value of (last) member 45: ', a_45)

# Calculating the first 10 members as a Python-list with subs-method
members1_10 = [a_n.subs(n, i) for i in range(1, 11)]

print('- First 10 members (subs-method): ', '\n', members1_10)

# Calculating the first 10 members with lambdifying
# transforming sympy expression a_n into numpy lambda-function f_n
f_n = sy.lambdify(n, a_n, "numpy")
list10 = np.arange(1, 11)  # creating numpy-ndarray of integers 1,2,...,9,10
# lambda-functions can take a numpy-ndarray as an input
members1_10 = f_n(list10)
# the output is also a numpy-ndarray
print('- First 10 members (lambdifying method): ''\n', members1_10)

# Solving equations
# creating a sympy-equation "a_n = input" with Eq-function
equation = sy.Eq(a_n, 28)
# solving the equation "a_n = input" with respect to n
index = sy.solve(equation, n)
if index:
    # the solution of solve-function will be a list-type object
    print('- The index of the member 28 is ', index)
    # the solution can be verified by substituting the index into a_n
    print(
        f'- Checking by replace n = {index[0]} into a_n, we have a_{index[0]} = ', a_n.subs(n, index[0]))
else:
    print('- The value 28 is NOT a member of the arithmetic sequence (n is not an integer).')

# Plot the graph of these first 10 members of the sequence:
# drawing a scatter-plot with matplotlib for a_n
plt.scatter(list10, members1_10, color='green')
plt.title("ARITHMETIC SEQUENCE")  # title of the whole plot
plt.xlabel("n")  # the title of x-axis
plt.ylabel("a_n")  # the title of y-axis
plt.grid(True)  # drawing the grid
plt.show()  # showing the actual plot

# -----------------------------------------------------------------------------------
# b) GEOMETRIC SEQUENCE:-------------------------------------------------------------
# -----------------------------------------------------------------------------------
# Choose q to be the last digit of your student number, which is not zero or one. [q = 4]
# Create the general term a_n of this geometric sequence. [a_n = 4*4**(n-1) = 4**n]
# Creating the general term of a geometric sequence
a_n = 4**n
print('- General Term of Arithmetic Sequence (with a1=7 and d=4): a_n = ', a_n)

# Calculating the member a_45 with subs-method
a_45 = a_n.subs(n, 45)
# the outcome is sympy-float number because the expression a_n had a float number 1.5
print('- Value of (last) member 45 (float form): ', a_45)
# nsimplify function will try to convert an expression into symbolic form
print('- Value of (last) member 45 (symbolic form): ', sy.nsimplify(a_45))
# Rational function will try to convert an expression into rational form
print('- Value of (last) member 45 (rational form): ', sy.Rational(a_45))

# Calculating the first 10 members as a Python-list with subs-method
members1_10 = [a_n.subs(n, i) for i in range(1, 11)]
print('- First 10 members (subs-method): ', '\n', members1_10)

# Solving equations
# creating a sympy-equation "a_n = 15740" with Eq-function
equation = sy.Eq(a_n, 15740)
# solving the equation "a_n = 15740" with respect to n
index = sy.solve(equation, n)
# the equation had no solutions, since n would not be an integer, so the list is empty
print('- The index of the member 15740 is ', index)
print('  --> The equation had no solutions, since n would not be an integer, so the list is empty!')

n = sy.symbols('n', real=True)  # changing the variable n to be a real variable
a_n = 4**n
equation = sy.Eq(a_n, 15740)
index = sy.solve(equation, n)
print('- If n is changed to Real number, the index of member 15740 is approx.= ',
      index)  # now we get the approximated solution
# function S() will keep the expression symbolic
index = sy.solve(sy.Eq((sy.S(4))**n, 15740), n)
print('- If keeping the expression symbolic, the index of member 15740 is ',
      index)  # now we get the symbolic solution
# method evalf() will change the expression into a float number with 15 digits
print('- If evlf to float number, the index of member 15740 is ',
      index[0].evalf())

# Drawing/plotting the graphs of sequences
# drawing a scatter-plot with matplotlib for a_n
plt.scatter(range(1, 11), members1_10, color='blue')
plt.title("Geometric sequence")  # title of the whole plot
plt.xlabel("n")  # the title of x-axis
plt.ylabel("a_n")  # the title of y-axis
plt.grid(True)  # drawing the grid
plt.show()  # showing the actual plot
