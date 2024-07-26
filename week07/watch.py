import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    start = r"(^<iframe)"
    pattern1 = r"(https?://(www\.)?youtube.com/embed/([a-zA-Z0-9]{11}))"
    matches = re.search(pattern1, s)
    matches2 = re.search(start, s)
    if matches and matches2:
        return "https://youtu.be/" + matches.group(3)


if __name__ == "__main__":
    main()
