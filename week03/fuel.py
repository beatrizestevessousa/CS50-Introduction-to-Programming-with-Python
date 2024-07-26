flag = False

while not flag:
    fraction = input("Fraction: ")

    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if not x > y and y != 0:
            flag = True
    except:
        flag = False

percentage = round(x / y * 100)
if percentage <= 1:
    print('E')
elif percentage >= 99:
    print('F')
else:
    print(f'{percentage}%')
