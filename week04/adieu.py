names = []
flag = True

while flag:
    try:
        n = input('Name: ')
        names.append(n)
    except:
        flag = False

print(f"Adieu, adieu, to {names[0]}", end="")

if len(names) == 2:
    print(" and "+names[1])
elif len(names) > 1:
    for i in range(1, len(names)-1):
        print(', ' + names[i], end="")

    print(", and "+names[-1])
