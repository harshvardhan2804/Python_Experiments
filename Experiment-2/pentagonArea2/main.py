import math

len = float(input("Enter the length of the pentagon: "))

area = (5*len*len)/(4*math.tan(3.14/5))


print("Area of pentagon is :"+str(area))