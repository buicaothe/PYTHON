# 5 LOOPS
while True:
    try:
        n = int(input('Enter non-negative integer n = '))
        if n >= 0:
            break
        else:
            print("This is no a non-negtive integer!")
    except ValueError:
        print('Not a NUMBER!!!!!')

for i in range(n):
    print(i*i)
