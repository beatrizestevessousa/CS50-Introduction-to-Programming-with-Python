import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not (sys.argv[1][-4:] == ".png" or sys.argv[1][-5:] == ".jpeg" or sys.argv[1][-4:] == ".jpg"):
        sys.exit("Not a JPEG/JPG/PNG file")

    if sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Files do not have the same extension")

    resize(sys.argv[1], sys.argv[2])

def resize(file1, file2):
    shirt = Image.open("shirt.png")
    size = shirt.size
    try:
        f1 = Image.open(file1)
        resized = ImageOps.fit(f1, size)
        resized.paste(shirt, mask=shirt)
        resized.save(file2)
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == '__main__':
    main()
