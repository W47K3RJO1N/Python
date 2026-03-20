nums = [1, 2, 2, 3, 4, 4, 5]

result = []

for i in nums:
    if nums.count(i) == 1:
        result.append(i)

print(result)
