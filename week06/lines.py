import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

try:
    lines = 0
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.lstrip()
            if not (line.startswith('#') or line == ''):
                lines += 1
except FileNotFoundError:
    sys.exit("File not found")

print(lines)
