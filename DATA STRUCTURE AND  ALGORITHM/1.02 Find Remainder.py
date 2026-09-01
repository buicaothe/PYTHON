# 1.02 Find Remainder
while True:
    try:
        a = int(input('Enter an integer number, a = ').strip())
        if 1 <= a:
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

while True:
    try:
        b = int(input('Enter an integer number, b = ').strip())
        if 1 <= b:
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

remainder = a % b
print(f"The remainder of {a} divided by {b} is: {remainder}")
