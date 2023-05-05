import math

len = int(input("Enter length of the pentagon:"))

s = 2 * len * math.sin(3.14/5)

area = (3*math.sqrt(3)*s*s)/2

print("Area of pentagon is :" +str(area))