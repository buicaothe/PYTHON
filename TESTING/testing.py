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

n = sy.symbols('n')  # changing the variable n to be a real variable
a_n = 4**n

# Solving equations
# creating a sympy-equation "a_n = 15740" with Eq-function
equation = sy.Eq(a_n, 15740)
# solving the equation "a_n = 15740" with respect to n
index = sy.solve(equation, n)
# the equation had no solutions, since n would not be an integer, so the list is empty
print('- The index of the member 15740 is ', index)
