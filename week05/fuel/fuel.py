def main():
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    try:
        x = int(x)
        y = int(y)
    except:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
       return f'{percentage}%'


if __name__ == "__main__":
    main()
