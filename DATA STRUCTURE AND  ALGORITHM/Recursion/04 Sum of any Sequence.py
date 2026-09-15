# Iterative:
def sum1(n):
    an=0
    for i in range(1,n+1):
        an = an+i
        print(i,'+')
    return an
print('Iterative :',sum1(5))

# Recursive:
def sum2(n):
    if i>n:
        return n
    return sum2(n,i+1)
