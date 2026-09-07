def sum(n):

    # base condition
    if n == 1:
        return 1

    return n + sum(n - 1)


n = 100
for i in range(n):
    print(f'{i+1}', end=' = ' if i == n-1 else ' + ')
print(sum(n))
