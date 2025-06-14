nums = [1,2,3,1,1,3]

counter = 0 

for i_idx, i in enumerate(nums):
    for j_idx, j in enumerate(nums):
        if i_idx == j_idx:
            continue
        else:
            if i_idx < j_idx and i == j:
                counter += 1
print(counter)