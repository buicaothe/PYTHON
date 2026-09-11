# 2. SUM
# a) Arithmetic sequence has a first member a_1 and a common difference d.
# Choose a_1 and d to be some numbers between 2-9.
# Calculate and print the sum of the first n members, where n is your age.
# Calculate this sum both with summation-function and with the arithmetic sum formula.
# Create and print also the expression of the symbolic sum of the first n members.
# You can choose the method of how you execute this.
# b) Geometric sequence has a first member a_1 and a common ratio q.
# Choose a_1 and q to be some numbers between 2-9.
# Create and print the expression of the symbolic sum of the first n members.
# You can choose the method of how you execute this.
# Solve the index variable n, when the sum equals S_n=10^6
# Print the index variable n as a floating point number.

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
# -----------------------------------------------------------------------------------
# a) ARITHMETIC SUM:------------------------------------------------------------
# -----------------------------------------------------------------------------------
n = sy.symbols('n')
a_n = 3+2*(n-1)

# Calculating sum (n = 45)
# calculating sum S_45 with sympy summation-function
sum45 = sy.summation(a_n, (n, 1, 45))
print('- Sum of a_n using Summation = ', sum45)
# calculating sum S_45 with the arithmetic sum formula
sum45 = 45*(a_n.subs(n, 1)+a_n.subs(n, 45))/2
print('- Sum of a_n using Arithmetic Sum Formula, S_45 = ', sum45)
print('- Application of Lambdify:')
f_n = sy.lambdify(n, a_n, "numpy")  # lambdifying the general term a_n into f_n
list45 = np.arange(1, 46)
print('* Index of the Sequence List45 = ', list45)
members1_45 = f_n(list45)
print('* Sequence a_n (now a List) = ', members1_45)
# calculating sum S_45 with numpy sum-function for sequence a_n
sum45 = np.sum(members1_45)
print('- Sum of a_n using Numpy Sum-function, S_45 = ', sum45)
sum45 = sum(members1_45)  # standard Python sum-function also works
print('- Standard Python sum-function S_45 = ', sum45)

# Calculating the symbolic sum of n members
# creating the general sum S_n with sympy summation-function
sum_n = sy.summation(a_n, (n, 1, n))
print('- General sum S_n with sympy summation-function = ', sum_n)
# creating the general sum S_n with the arithmetic sum formula
sum_n = n*(a_n.subs(n, 1)+a_n)/2
print('- General sum S_n with Arithmetic Sum formula = ', sum_n)

# Solving equations
equation = sy.Eq(sum_n, 420)
# solving the index variable n, when sum equals S_n=420
index = sy.solve(equation, n)
print('- Index n when Sum_n = 240, n = ', index)
print('- Result verification, Sum_n = ',
      sum_n.subs(n, index[0]))  # verifying the result

# Plotting sum S_10 as a 1-width histogram
plt.bar(list45, members1_45, width=1.0, color='g', edgecolor='black')
plt.title("Arithmetic Sum S_45")
plt.xlabel("n")
plt.ylabel("a_n")
plt.show()

# -----------------------------------------------------------------------------------
# b) GEOMETRIC SUM:------------------------------------------------------------
# -----------------------------------------------------------------------------------
