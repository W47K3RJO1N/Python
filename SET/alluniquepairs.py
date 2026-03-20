nums = [1, 2, 3, 4]
pairs = set()

for i in nums:
    for j in nums:
        if i != j:
            pairs.add((i, j))

print(pairs)
