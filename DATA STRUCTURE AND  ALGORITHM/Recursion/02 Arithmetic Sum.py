
def sum(n):
    if n <= 3:
        return 3
    print(n)
    return sum(n-3)+n


print(sum(9))
