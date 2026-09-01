# 1.05 Area and perimeter of Circular Plot
import math
while True:
    try:
        r = float(input('Enter the Radius of the Circular Plot, r = '))
        if r > 0:
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')
area = math.pi*(r**2)
perimeter = 2*math.pi*r
print(f'Area of a Circular Plot with Radius {r} is {area}.')
print(f'Perimeter of a Circular Plot with Radius {r} is {perimeter}.')
