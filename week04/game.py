from random import randint

valid = False

while not valid:
    n = input('Level: ')
    try:
        n = int(n)
    except:
        continue

    if n > 0:
            valid = True

number = randint(1, n)

guessed = False

while not guessed:
    g = input('Guess: ')
    try:
        g = int(g)
    except:
        continue

    if g > 0:
            if g == number:
                print('Just right!')
                guessed = True
            elif g < number:
                print('Too small!')
            else:
                print('Too large!')
