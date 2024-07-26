calc = input('Expression: ').split(' ')

if calc[1] == '+':
    result = float(int(calc[0]) + int(calc[2]))
elif calc[1] == '-':
    result = float(int(calc[0]) - int(calc[2]))
elif calc[1] == '*':
    result = float(int(calc[0]) * int(calc[2]))
else:
    result = float(int(calc[0]) / int(calc[2]))

print(result)
