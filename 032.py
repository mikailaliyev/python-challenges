# Ask for the radius and the depth of a cylinder 
# and work out the total volume (circle area*depth) rounded to three decimal places.
import math

radius_of_circle = int(input("Enter the radius of a cylinder\n"))
depth = int(input("Enter the depth of the cylinder\n"))
area_of_circle = math.pi * (radius_of_circle ** 2)
total_volume = area_of_circle * depth
print(round(total_volume, 3))
