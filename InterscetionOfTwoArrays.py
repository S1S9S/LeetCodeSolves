nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

result = []

nums1 = set(nums1)
nums2 = set(nums2)

for i in nums1:
    for j in nums2:
        if i == j:
            result.append(i)
print(result)