# 1.07 Area of a Square:

while True:
    try:
        a = float(input('Enter the side of square, a = '))
        if a > 0:
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

area = a*a
print(f"Area of the square with side a = {a} is: {area:.2f}")
