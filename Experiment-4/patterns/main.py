# pattern 1

# for i in range(0,6):
#     for j in range(0,i+1):
#         print(j+1,end="")
#
#     print()

# pattern 2


# for i in range(0,6):
#     for j in range(0,6-i):
#         print(j+1,end="")
#
#     print()

# pattern 3


# decr = 8
# for i in range(5):
#     count = 0
#     for k in range(decr):
#         print(end=" ")
#     decr = decr - 2
#     for j in range(i+1):
#         count = count + 1
#     num = count
#     for j in range(i+1):
#         print(num, end=" ")
#         num = num - 1
#     print()

# pattern 4

n=int(input("Enter the number of rows\n"))
i=1

while(i<=n):
    #space printing
    space=i-1
    while(space):
        print(" ",end="")
        space=space-1


    #2nd trinagle printing
    j=1
    count=n-i+1
    while(count):
        print(count,end="")
        j=j+1
        count=count-1

    #3rd triangle printing
    count=n-i
    val=2
    while(count):
        print(val,end="")
        val=val+1
        count=count-1


    print("")
    i=i+1


