n = 3
for i in range(n):
    for j in range(9):
        if (i + j) % 4 == 0 or (i == 1 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
