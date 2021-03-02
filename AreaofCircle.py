#program to find the area of the circle with given radius.

#PI = 3.14
import math

r = float(input("Enter the radius of the circle: "))

#area = PI * r * r
area = math.pi * r * r
print("%.16f" %area)