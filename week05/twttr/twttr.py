def main():
    text = input()
    print(shorten(text))


def shorten(text):
    new_text = ''
    for letter in text:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_text += letter
    return new_text


if __name__ == "__main__":
    main()
