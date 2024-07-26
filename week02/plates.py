from string import punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    r = length(s) + beggining(s) + middle(s)
    return True if r == 3 else False

def length(s):
    return 1 if 2 <= len(s) <= 6 else 0

def beggining(s):
    return 1 if s[:2].isalpha() else 0

def middle(s):
    first_number = -1
    for n in range(len(s)):
        if s[n] in punctuation:
            return 0
        if s[n].isdecimal() and first_number == -1:
            if s[n] == '0':
                return 0
            first_number = n
    return 1 if s[first_number:].isdecimal() or first_number == -1 else 0

main()
