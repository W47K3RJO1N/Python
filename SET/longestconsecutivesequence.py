nums = [100, 4, 200, 1, 3, 2]

num_set = set(nums)
longest = 0

for num in num_set:
    if num - 1 not in num_set:
        length = 1
        while num + length in num_set:
            length += 1
        
        longest = max(longest, length)

print("Longest sequence:", longest)
