nums = [1, 2, 4, 5] 
n = 5

full = set(range(1, n+1))

missing = full - set(nums)

print("Missing number:", missing)
