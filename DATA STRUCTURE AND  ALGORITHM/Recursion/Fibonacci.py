# CALCULATING FIBONACCI LAST MEMBER:
while True:
    try:
        n = int(input('- Enter the index number of the, n = ').strip())
        if n >= 1:
            break
        else:
            print('The number should be greater than 0! Please re-type:')
    except ValueError:
        print('Not a Number!')

# OPTION 1 - ITERATIVE ALGORITHM:


def fibo1():
    if n <= 1:
        return 1

    a = 0
    b = 1
    for i in range(2, n + 1):
        temp = a
        a = b
        b = temp + b
    return b


print(f'--> The Fibonacci at certain index {n}, F({n}) = ',
      fibo1(), ' (using INTERATIVE ALGORITHM)')

# OPTION 2 - RECURSIVE ALGORITHM:


def fibo2(n):
    if n <= 2:
        return 1
    return fibo2(n-2)+fibo2(n-1)


print(f'--> The Fibonacci at certain index {n}, F({n}) = ',
      fibo2(n), ' (using RECURSIVE ALGORITHM)')
