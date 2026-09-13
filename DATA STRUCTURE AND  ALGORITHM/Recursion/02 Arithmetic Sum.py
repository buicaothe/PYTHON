# ARITHMETIC SUM:

n = int(input('- Enter Number of members for Arithmetic Sum: n = '))
a1 = int(input('- Enter first member for Arithmetic Sum: a1 = '))
d = int(input('- Enter common diffrence of the Sequence, d = '))

# -----------------------------------------------------------------------------
# 3.1 - CALCULATE LAST MEMBER (an) OF SEQUENCE:--------------------------------
# -----------------------------------------------------------------------------
print('*** 3.1 CALCULATE LAST MEMBER (an) OF SEQUENCE:')

# OPTION 1 - ITERATIVE ALGORITHM:


def an_iterative():
    an = a1
    for i in range(1, n):
        an = an+d
    return an


print('- The last member of using ITERATIVE ALGORITHM, an = ', an_iterative())

# OPTION 2 - RECURSIVE ALGORITHM:


def an_recursive(n):
    if n <= 1:
        return a1
    return an_recursive(n-1)+d


print('- The last member of using RECURSIVE ALGORITHM, an = ', an_recursive(n))

# OPTION 3 - USING FORMULA:


def an_formula():
    return a1+d*(n-1)


print('- The last member of using FORMULA, an = ', an_formula())
# Compare the runtime of both by using Jupyter's built-in tool %timeit:
print('Compare the runtime:')
print('3.1.1) Runtime of Iterative Algorithm:')
%timeit an_iterative()
print('3.1.2) Runtime of Recursive Algorithm:')
%timeit an_recursive(n)
print('3.1.3) Runtime of using Formula:')
%timeit an_formula()

# -----------------------------------------------------------------------------
# 3.2 - CALCULATE SUM:---------------------------------------------------------
# -----------------------------------------------------------------------------
print('*** 3.2 CALCULATE SUM:')
# Define sequence:
sequence = []
for i in range(1, n+1):
    sequence.append(a1+d*(i-1))
print('The Arithmetic Sequence an = ', sequence)

# OPTION 1 - ITERATIVE ALGORITHM:


def arithmetic_sum1():
    total = 0
    for i in sequence:
        total += i
    return total


print('- Geometric Sum by ITERATIVE ALGORITHM = ', arithmetic_sum1())

# OPTION 2 - RECURSIVE ALGORITHM:


def arithmetic_sum2(n):
    if n <= 1:
        return a1
    return arithmetic_sum2(n-1)+sequence[n-1]


print('- Arithmetic Sum by RECURSIVE ALGORITHM = ', arithmetic_sum2(n))

# OPTION 3 - USING FORMULA:


def arithmetic_sum3():
    return n*(a1+sequence[n-1])/2


print('- Arithmetic Sum by using FORMULA = ', arithmetic_sum3())

# Compare the runtime of both by using Jupyter's built-in tool %timeit:
print('Compare the runtime:')
print('3.2.1) Runtime of Iterative Algorithm:')
%timeit arithmetic_sum1()
print('3.2.2) Runtime of Recursive Algorithm:')
%timeit  arithmetic_sum2(n)
print('3.2.3) Runtime of using Formula:')
%timeit arithmetic_sum3()
