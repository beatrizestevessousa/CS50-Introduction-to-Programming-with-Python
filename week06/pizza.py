import sys
from csv import reader
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try:
    table = []
    with open(sys.argv[1], "r") as file:
        lines = reader(file)
        for line in lines:
            table.append(line)
        print(tabulate(table[1:], table[0], tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File not found")
