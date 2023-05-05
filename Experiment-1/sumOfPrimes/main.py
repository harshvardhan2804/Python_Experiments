a= int(input("Enter a number:"))
sum = 0

for i in range(2, a + 1):
    flag = 0
    for j in range(1, i + 1):
        if (i % j == 0 and j != 1 and j != i):
            flag = 1
            break

    if (flag == 0):
        sum += i

print("The sum is:" + str(sum))
