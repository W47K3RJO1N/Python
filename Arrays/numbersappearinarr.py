arr = [1, 2, 3, 2, 4, 2, 5]
num = 2
count = 0

for i in arr:
    if i == num:
        count += 1

print("Number appears", count, "times")
