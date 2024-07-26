text = input('Input: ')
print('Output: ', end='')

for letter in text:
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        print(letter, end='')
