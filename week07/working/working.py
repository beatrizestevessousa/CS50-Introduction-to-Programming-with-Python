import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"((1?[0-9])(:[0-5][0-9])? (AM|PM) to (1?[0-9])(:[0-5][0-9])? (AM|PM))"
    matches = re.search(pattern, s, re.IGNORECASE)
    if matches:
        houra = int(matches.group(5))
        perioda = matches.group(7)
        hourb = int(matches.group(2))
        periodb = matches.group(4)
        if not hourb == 12:
            if periodb == 'PM':
                hourb += 12
        else:
            if periodb == 'AM':
                hourb = 0
        if not houra == 12:
            if perioda == 'PM':
                houra += 12
        else:
            if perioda == 'AM':
                houra = 0
        if not matches.group(3) and not matches.group(6):
            return f"{hourb:02}:00 to {houra:02}:00"
        if not matches.group(3):
            return f"{hourb:02}:00 to {houra:02}{matches.group(6)}"
        if not matches.group(6):
            return f"{hourb:02}{matches.group(3)} to {houra:02}:00"
        return f"{hourb:02}{matches.group(3)} to {houra:02}{matches.group(6)}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
