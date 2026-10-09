


import math
def circle_stas(radius):
    area = math.pi * (radius**2)
    circ = 2 * math.pi * radius
    return area, circ

r = int(input("Enter Radius: "))
area, circ = circle_stas(radius = r)

print(f"Radius:        {r:.0f}")
print(f"Area:          {area:.2f}")
print(f"Circumference: {circ:.2f}")