



def isPerfect(num,sum):
    if sumOfDivisors(num) == sum :
        return True
    else:
        return False


def sumOfDivisors(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0 :
            sum += i


    return sum

ans =[]
for i in range(1,10000):
   if isPerfect(i,i)==True:
       ans.append(i)


print(ans)