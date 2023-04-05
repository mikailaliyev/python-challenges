# Ask the user to enter the radius of a circle (measurement from the centre point to the edge). 
# Work out the area of the circle (π*radius2).
import math

radius_of_circle = int(input("Enter the radius of a circle\n"))
area_of_circle = math.pi * (radius_of_circle ** 2)
print(area_of_circle)
