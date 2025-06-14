candies = [2,3,5,1,3]

extraCandies = 3

result = []

max = 0 

for i in candies:
    if i > max:
        max = i

for j in candies:
    if j + extraCandies >= max:
        result.append("true")
    else:
        result.append("false")

print(result)