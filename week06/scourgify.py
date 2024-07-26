import sys
from csv import DictReader, DictWriter

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")

    splitting(sys.argv[1], sys.argv[2])

def splitting(file1, file2):
    try:
        with open(file1, "r") as file1:
            with open(file2, "w") as file2:
                fieldnames = ['first', 'last', 'house']
                lines = DictReader(file1)
                writer = DictWriter(file2, fieldnames=fieldnames)
                writer.writeheader()
                for line in lines:
                    writer.writerow({'first':line['name'].split(', ')[1], 'last':line['name'].split(', ')[0], 'house':line['house']})
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == '__main__':
    main()
