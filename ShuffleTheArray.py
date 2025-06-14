nums = [2,5,1,3,4,7]
n = 3
h = 0
total = []

for i in range(n):
    total.append(nums[i])
    for j in range(n, len(nums)):
        j += h
        total.append(nums[j])
        break
    h += 1
print(total)