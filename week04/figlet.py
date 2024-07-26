import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

if len(sys.argv) > 1:
    if sys.argv[1] in ['-f', '--font']:
        if sys.argv[2] in figlet.getFonts():
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')
else:
    text = input("Input: ")
    figlet.setFont(font = choice(figlet.getFonts()))
    print(figlet.renderText(text))
