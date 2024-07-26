from random import randint


def main():
    level = get_level()
    print(f'Score: {generate_integer(level)}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except:
            continue
        if 1 <= level <= 3:
            return level

def generate_integer(level):
    score = 10
    for i in range(10):
        # Flags
        wrong = 0
        correct = False

        if level == 1:
            lower_bound = 0
        else:
            lower_bound = 10**(level-1)

        # Generate random numbers with correct bounds
        n1 = randint(lower_bound, (10**level)-1)
        n2 = randint(lower_bound, (10**level)-1)

        # Prompt the question until the user inputs the wrong answer 3 times or until it get correct before the 3 attempts
        while wrong < 3 and not correct:

            # Check if user inputs an integer
            try:
                answer = int(input(f'{n1} + {n2} = '))
            except:
                wrong += 1
                print('EEE')
                continue

            # If integer, see if answer is correct
            if answer != n1+n2:
                wrong += 1
                print('EEE')
            else:
                correct = True

        # Check if the user got one wrong attempt and update his/hers score
        if wrong > 0:
            score -= 1
            # Display the result if the 3 attempts were used
            if wrong == 3:
                print(f'{n1} + {n2} = {n1+n2}')
    return score



if __name__ == "__main__":
    main()
