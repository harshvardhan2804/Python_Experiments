

def cramerRule(a,b,c,d,e,f):
    numerator_1 = e*d - b*f
    numerator_2 = a*f - e*c
    denominator = a*d -b*c

    if denominator==0:
        print("equation has no roots")
    else:
        print("solution of the eqations are:")
        print(float(numerator_1/denominator))
        print(float(numerator_2 / denominator))





a = int(input("Enter a num:"))
b = int(input("Enter b num:"))
c = int(input("Enter c num:"))
d = int(input("Enter d num:"))
e = int(input("Enter e num:"))
f = int(input("Enter f num:"))

print(cramerRule(a,b,c,d,e,f,))
