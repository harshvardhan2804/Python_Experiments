n = 7
for i in range(1, n):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print(2**j, end="")
    for j in range(i-2, -1, -1):
        print(2**j, end="")
    print("")
