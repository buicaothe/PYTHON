# 1.10 Volume and surface area of sphere:
import math

while True:
    try:
        r = float(
            input('Enter the radius, r = '))
        if (r > 0):
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

volume = (4/3) * math.pi * (r**3)
surface_area = 4 * math.pi*(r**2)

print(f"Radius of Sphere: {r}")
print(f"Volume of Sphere: {volume:.2f}")
print(f"Surface area of Sphere: {surface_area:.2f}")
