

def isValid(a,b,c):
    if(a+b>c and b+c > a and c+a > b):
        return True
    else:
        return False

def perimeterOfTriangle(a,b,c):
    if(isValid(a,b,c)):
        print("perimeter of triangle is : " + str(a+b+c))
    else:
        print("Invalid sides :)")


side1 = int(input("Enter first side:"))
side2 = int(input("Enter second side:"))
side3 = int(input("Enter third side:"))

print(perimeterOfTriangle(side1,side2,side3))