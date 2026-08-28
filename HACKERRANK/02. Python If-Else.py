# 2. PYTHON IF-ELSE:
while True:
    try:
        n = int(input('Enter an integer number from 1 to 100, n = ').strip())
        if 1 <= n <= 100:
            break
        else:
            print('The number should be from 1 to 100! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

if n % 2 != 0:
    print('Weird')
elif 2 <= n <= 5:
    print('Not Weird')
elif 6 <= n <= 20:
    print('Weird')
else:
    print('Not Weird')
