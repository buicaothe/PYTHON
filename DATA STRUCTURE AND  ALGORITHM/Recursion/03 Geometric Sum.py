# GEOMETRIC SUM

n = int(input('- Enter Number of members for Geometric Sum: n = '))
a1 = int(input('- Enter first member for Geometric Sum: a1 = '))
q = int(input('- Enter common ratio of the Sequence, q = '))
an = a1*q**(n-1)
print('- The Final member of the Geometric Sequence, an = ', an)

sequence = []
for i in range(1, n+1):
    sequence.append(a1*q**(i-1))
print('- The Geometric Sequence an = ', sequence)

# ITERATIVE ALGOITHM:


def geometric_sum1():
    total = 0
    for i in sequence:
        total += i
    return total


print('- Geometric Sum by ITERATIVE ALGORITHM = ', geometric_sum1())

# RECURSIVE ALGOITHM:


def geometric_sum2(n):
    if n <= 1:
        return a1
    return geometric_sum2(n - 1) + sequence[n - 1]


print('- Geometric Sum by RECURSIVE ALGORITHM = ', geometric_sum2(n))
