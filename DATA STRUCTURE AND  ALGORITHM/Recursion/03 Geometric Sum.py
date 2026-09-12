def sum1(n):
    if n <= 1:
        return 1
    return sum1(n/4)+n


print('- Geometric Sum = ', sum1(16))


n = int(input('- Enter Number of members for Arithmetic Sum: n = '))
a1 = int(input('- Enter first member for Arithmetic Sum: a1 = '))
d = int(input('- Enter common diffrence of the Sequence, d = '))
an = a1+d*(n-1)
print('- The Final member of the Arithmetic Sequence, an = ', an)

sequence = []
for i in range(1, n+1):
    sequence.append(a1+d*(i-1))
print('- The Arithmetic Sequence an = ', sequence)


def sum2(an):
    if an <= a1:
        return a1
    return sum2(an-d)+an


print('- Arithmetic Sum = ', sum2(an))
