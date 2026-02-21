n = 5
for i in range(n, 0, -1):
    for j in range(1, 2*n):
        if i == n or j == n-i+1 or j == n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
