# Iterative:
def sum1(n):
    an=0
    for i in range(1,n+1):
        an = an+i
        print(i,'+')
    return an
print('Iterative :',sum1(101))

# Recursive:
def sum2(n):
    if n <=1:
        return 1
    return sum2(n-1)+n
print('Recrusive :',sum2(101))