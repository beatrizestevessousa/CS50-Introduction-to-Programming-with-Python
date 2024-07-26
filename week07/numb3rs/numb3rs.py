import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
          r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
          r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
          r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"

    matches = re.search(pattern, ip)
    if matches:
        return True
    return False


if __name__ == "__main__":
    main()
