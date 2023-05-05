# Experiment-4


#Question-1
# def findDistance(num):
#    return 1.609 * num
#
#
# for i in range(1,11):
#    print(i,end="   ")
#    print(findDistance(i))



# #Question-2

# count=int(10000)
# for i in range (1,11):
#    increment=float(0.05*count)
#    count=count+increment
#
# print("The tution after ten years will be "+str(count))
# sum=int(0)
#
# for i in range(1,5):
#    sum=sum+count
#    increment=float(0.05*count)
#    count=count+increment
#
# print("The total cost of tution afterten years for four year course "+str(sum))
#

# #Question-3


# count = 0
# for i in range(100, 1001):
#    if i % 5 == 0 and i % 6 == 0:
#        count += 1
#        print(i, end=' ')
#        if count % 10 == 0:
#            print()
#
#

# #Question-4
#
# count = 0
# for i in range(33, 127):
#    count += 1
#    print(chr(i), end=' ')
#    if count % 10 == 0:
#        print()



# #Question-5
# # pattern-1
# for i in range(0,6):
#    for j in range(0,i+1):
#        print(j+1,end="")
#
#    print()
#
# #pattern-2
#
# for i in range(0,6):
#    for j in range(0,6-i):
#        print(j+1,end="")
#
#    print()
#
# #pattern-3
#
# decr = 8
# for i in range(5):
#    count = 0
#    for k in range(decr):
#        print(end=" ")
#    decr = decr - 2
#    for j in range(i+1):
#        count = count + 1
#    num = count
#    for j in range(i+1):
#        print(num, end=" ")
#        num = num - 1
#    print()
#
# #pattern-4
# n=int(input("Enter the number of rows\n"))
# i=1
# while(i<=n):
#    #space printing
#    space=i-1
#    while(space):
#        print(" ",end="")
#        space=space-1
#
#
#    #2nd triangle printing
#    j=1
#    count=n-i+1
#    while(count):
#        print(count,end="")
#        j=j+1
#        count=count-1
#
#    #3rd triangle printing
#    count=n-i
#    val=2
#    while(count):
#        print(val,end="")
#        val=val+1
#        count=count-1
#
#
#    print("")
#    i=i+1

#question 6(odd roll number)

# n = 5
#
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(1, n-i+1):
#         print(j, end=" ")
#     for j in range(n-i, 0, -1):
#         print(j, end=" ")
#     print()
