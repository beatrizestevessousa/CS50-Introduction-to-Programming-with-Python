from datetime import date
import sys
import inflect
import operator


def main():
    try:
        born = input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(born))
        print(calc_diff(difference.days))
    except ValueError:
        sys.exit("Invalid date")


def calc_diff(difference):
    p = inflect.engine()
    difference_in_minutes = difference * 24 * 60
    return f"{(p.number_to_words(difference_in_minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
