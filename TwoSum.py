nums = [3,2,4]
target = 6
seen = {}
for idx ,i in enumerate(nums):
    complement = target - i
    if complement in seen:
        print([seen[complement], idx])
    seen[i] = idx