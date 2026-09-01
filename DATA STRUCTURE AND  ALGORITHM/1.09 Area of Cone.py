# 1.09 Surface Area of Cone
import math

while True:
    try:
        radius = float(
            input('Enter the radius, r = '))
        height = float(
            input('Enter the Height, h = '))
        if (radius > 0) and (height > 0):
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

slant_height = math.sqrt(radius ** 2 + height ** 2)
surface_area = math.pi * radius * (radius + slant_height)

print(f"Radius: {radius}, Height: {height}")
print(f"Surface area of the Cone: {surface_area:.2f}")
