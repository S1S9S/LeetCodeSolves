accounts = [[1,2,3], [3,4,5], [1,8,2]]
balance = 0

for account in accounts:
    temp = 0
    tempAccount = account
    for i in tempAccount:
        temp += i
        if balance <= temp:
            balance = temp
print(balance)