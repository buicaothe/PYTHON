# 1.06 Area of a triangle based on the length of three sides:

import math
while True:
    try:
        a = float(input('Enter the side of triangle, a = '))
        b = float(input('Enter the side of triangle, b = '))
        c = float(input('Enter the side of triangle, c = '))
        if (a > 0) and (b > 0) and (c > 0):
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Three sides of the triangle a = {a}, b = {b}, c = {c}")
print(f"Area of the TRiangle: {area:.2f}")
