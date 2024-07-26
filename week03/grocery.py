flag = False
groceries = {}

while not flag:
    try:
        item = input().upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except:
        flag = True

groceries = sorted(groceries.items())
for key in groceries:
    print(key[1], key[0])
