weight=float(input("Enter the amount of water in kg:"))
itemp=float(input("Enter the initial temp of water:"))
ftemp=float(input("Enter the final temp of water:"))

ans=float(weight*(ftemp-itemp)*4184)
print("The energy required in joules is:"+str(ans))