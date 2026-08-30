# PRINT FUNCTIONS:
while True:
    try:
        n = int(input('Enter a integer from 1 to 150, n = '))
        if 1 <= n <= 150:
            break
        else:
            print("This is no as possitive integer!")
    except ValueError:
        print('Not a NUMBER!!!!!')

for i in range(n):
    print(i+1, end='')
