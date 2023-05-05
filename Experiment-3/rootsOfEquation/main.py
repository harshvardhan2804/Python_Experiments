
import  math
def rootsOfEquation(a,b,c) :
     disc = math.pow(b,2) - 4*a*c

     if(disc == 0):
         print("roots are equal")
         ans = float(-1*b/2*a)
         print(ans)

     elif(disc >0):
         print("roots are real and distinct")
         r1 = (-1*b + math.sqrt(disc))/(2*a)
         r2 = (-1*b - math.sqrt(disc))/(2*a)
         print(r1)
         print(r2)
     else:
         print("roots are imaginary")


print("Enter three numbers which are coeff of  quadratic equation:")

a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))

print(rootsOfEquation(a,b,c))
