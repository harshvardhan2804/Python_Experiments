count = 0
for i in range(33, 127):
    count += 1
    print(chr(i), end=' ')
    if count % 10 == 0:
        print()
