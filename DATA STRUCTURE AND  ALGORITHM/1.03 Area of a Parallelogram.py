# 1.03 Area of a Parallelogram:

while True:
    try:
        b = float(input('Enter the base of the Parallelogram, b = '))
        h = float(input('Enter the height of the Parallelogram, h = '))
        if b*h > 0:
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

area = b*h
print(f'The Area of a Parallelogram base {b} and height {h} is {area}.')
