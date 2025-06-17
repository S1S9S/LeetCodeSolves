nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

answer = []
nums1 = set(nums1)
nums2 = set(nums2)

for i in list(nums1):
    for j in list(nums2):
        if i == j:
            nums1.remove(i)
            nums2.remove(i)
answer.append(list(nums1))
answer.append(list(nums2))

print(answer)