# 3 ARITHMATIC OPERATORS:
while True:
    try:
        a = int(input('Enter a = ').strip())
        if 1 <= a <= 10**10:
            break
        else:
            print('The number a should be from 1 to 10^10! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

while True:
    try:
        b = int(input('Enter b = ').strip())
        if 1 <= b <= 10**10:
            break
        else:
            print('The number b should be from 1 to 10^10! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

sum = a+b
difference = a-b
product = a*b
print(sum)
print(difference)
print(product)
