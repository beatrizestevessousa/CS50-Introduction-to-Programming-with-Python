text = input('camelCase: ')
result = ''

for letter in text:
    if letter.isupper():
        letter = '_' + letter.lower()
    result += letter

print('snake_case:', result)
