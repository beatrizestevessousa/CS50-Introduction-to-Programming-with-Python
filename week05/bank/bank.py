def main():
    greeting = input('Greeting: ')
    print(f'${value(greeting)}')


def value(greeting):

    if 'hello' in greeting.lower():
        price = 0
    elif greeting[0].lower() == 'h':
        price = 20
    else:
        price = 100

    return price

if __name__ == "__main__":
    main()
