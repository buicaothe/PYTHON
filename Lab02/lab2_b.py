# HOW MANY INTERSECTION POINTS DOES A LINE AND AN ELLIPSE HAVE?

#1. Input for the Line:
print('1. Inputs for the line | y = mx + c:')
m = float(input('Enter m = '))
c = float(input('Enter c = '))

#2. Input for the Ellipse:
print('2. In put for the Ellipse | (x-h)^2/a^2 + (y-k)^2/b^2 = 1:')
a = float(input('Enter the ellipse semi-width a = '))
b = float(input('Enter the ellipse semi-height b = '))
h = float(input('Enter the center x coordinate h = '))
k = float(input('Enter the center y coordinate k = '))

#3. Find A,B,C for Equation Ax^2 + Bx + C = 0
A = float((a**2)*(m**2) + (b**2))
B = float(2*(a**2*m*(c-k) - (b**2)*h))
C = float((a**2)*(c-k)**2 + (b**2)*(h**2)-(a**2)*(b**2))

#4. CALCULATE THE D = B^2-4AC
D = B**2 - 4*A*C
print('The Delta of Equation (Ax^2 + Bx + C = 0) is D = ',D)

# Calculate intersection points:
x1 = (-B+(D)**0.5)/(2*A)
x2 = (-B-(D)**0.5)/(2*A)
y1 = m*x1+c
y2 = m*x2+c

#5. How many intersection points:
print('How many intersection points:')
if D < 0:
    print('D < 0:')
    print('No intersection!')
else:
    if D == 0:
        print('D = 0:')
        print('One Point intersection!', 'at (',x1,',',y1,')')

    else:
        print('D > 0:')
        print('Two Point intersection!', 'at (',x1,',',y1,')',' and ','(',x2,',',y2,')')

#_________________DRAW THE LINE AND ELLIPSE_________________
#  Bring libraries and give them shorter names
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

# Create figure and axels
fig, ax = plt.subplots()

#  Create ellipse center point (h, k), width a, height b, angle 0 degrees
ellipse = Ellipse((h, k), width = 2*a, height = 2*b, angle = 0, color='green')

#  Add ellipse to drawing area
ax.add_patch(ellipse)

#  set limits to exis
ax.set_xlim(-10, 20)
ax.set_ylim(-10, 20)

#  Define line 
#  linspace creates x values 
#  from selected range
x = np.linspace(-10, 20, 2)
#  Line's equation to get y values
y = m*x + c

#  Draw line
plt.plot(x, y, color='red')

#  Figure's title and axis titles
plt.title("Line and ellipse")
plt.xlabel("x")
plt.ylabel("y")
#  Show grid
plt.grid(True)

# Show figure
plt.show()
