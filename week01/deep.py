answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').strip()

if answer == '42' or answer.replace('-', ' ').lower() ==  'forty two':
    print('Yes')
else:
    print('No')
