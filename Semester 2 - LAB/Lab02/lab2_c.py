# _____________LAB2_C____________
# AI Tool: Gemini (Google)
# Prompts used:
    # Write Python Code program to solve the following issue: 
    # How many intersection points does a line and an ellipse have? The line equation y = mx+c 
    #   (ask the user to input all the parameters m and c)
    # the ellipse equation is ((x-h)^2)/a^2 + (y-k)^2)/b^2 = 1 
    #   (ask the user to input all the parameters h, k, a, and b). 
    # The program prints how many intersection points and prints the intersection point(s) or a message "no intersection". 
    # Also draw the figures (the line and the ellipse).

import numpy as np
import matplotlib.pyplot as plt

def solve_intersection():
    print("--- Intersection of Line and Ellipse ---")
    try:
        # User Inputs
        m = float(input("Enter line slope (m): "))
        c = float(input("Enter line y-intercept (c): "))
        h = float(input("Enter ellipse center x (h): "))
        k = float(input("Enter ellipse center y (k): "))
        a = float(input("Enter semi-major axis (a): "))
        b = float(input("Enter semi-minor axis (b): "))
        
        if a <= 0 or b <= 0:
            print("Error: Axes a and b must be positive.")
            return
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    # Quadratic coefficients for Ax^2 + Bx + C = 0
    # Derived by substituting y = mx + c into ((x-h)^2)/a^2 + ((y-k)^2)/b^2 = 1
    # Simplified form:
    A = (1/a**2) + (m**2/b**2)
    B = (-2*h/a**2) + (2*m*(c-k)/b**2)
    C = (h**2/a**2) + ((c-k)**2/b**2) - 1

    # Discriminant
    D = B**2 - 4*A*C

    points = []
    print("\n--- Results ---")
    
    if D < 0:
        print("0 intersection points: No intersection.")
    elif abs(D) < 1e-12: # Check for zero with floating point tolerance
        print("1 intersection point (Tangent):")
        x = -B / (2*A)
        y = m*x + c
        points.append((x, y))
        print(f"Point: ({x:.4f}, {y:.4f})")
    else:
        print("2 intersection points:")
        x1 = (-B + np.sqrt(D)) / (2*A)
        x2 = (-B - np.sqrt(D)) / (2*A)
        for x in [x1, x2]:
            y = m*x + c
            points.append((x, y))
            print(f"Point: ({x:.4f}, {y:.4f})")

    # --- Plotting ---
    # Create ellipse points using parametric equations
    t = np.linspace(0, 2*np.pi, 500)
    ex = h + a * np.cos(t)
    ey = k + b * np.sin(t)

    # Create line points
    # Dynamically scale line range based on ellipse center and size
    x_range = np.linspace(h - 2*a, h + 2*a, 100)
    ly = m * x_range + c

    plt.figure(figsize=(8, 8))
    plt.plot(ex, ey, label='Ellipse', color='blue', linewidth=2)
    plt.plot(x_range, ly, label=f'Line: y={m}x+{c}', color='red', linestyle='--')

    # Plot intersection points
    for p in points:
        plt.plot(p[0], p[1], 'go', markersize=10, label='Intersection')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.axis('equal')
    plt.title('Line and Ellipse Visualization')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    solve_intersection()