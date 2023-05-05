import math

x1=float(input("Enter x coordinate of first point:"))
y1=float(input("Enter y coordinate of first point:"))
x2=float(input("Enter x coordinate of second point:"))
y2=float(input("Enter y coordinate of second point:"))
var1=float(pow((x1-x2),2))
var2=float(pow((y1-y2),2))
ans=float(pow((var1+var2),0.5))
print("The distance between points is:"+str(ans))