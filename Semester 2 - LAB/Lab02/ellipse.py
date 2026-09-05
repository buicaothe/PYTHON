#  Bring libraries and give them shorter names
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

# Create figure and axels
fig, ax = plt.subplots()

#  Create ellipse center point (5, 5), width 10, height 5, angle 30 degrees
ellipse = Ellipse((5, 5), width=10, height=5, angle=30, color='green')

#  Add ellipse to drawing area
ax.add_patch(ellipse)

#  set limits to exis
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

#  Define line 
#  linspace creates x values 
#  from selected range
x = np.linspace(-10, 10, 30)
#  Line's equation to get y values
y = -2*x + 5

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
