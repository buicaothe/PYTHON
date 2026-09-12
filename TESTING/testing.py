def func(n):
    if n <= 0:
        return 1
    return n*func(n-1)


n = 5
print(func(5))


f = 1
i = 2
n = 5
# Calculating factorial of number
while (i <= n):
    f = i*f
    i = i+1
print(f)

f = 1
n = 5
# Calculating factorial of number
for i in range(1, n+1):
    f = i*f
    i = i+1
print(f)
