from sys import exit, argv
from pyfiglet import Figlet
import random

figlet = Figlet()
lists = figlet.getFonts()

if len(argv) == 1:
    figlet.setFont(font=random.choice(lists))
    text = input("Input: ")
    txt = figlet.renderText(text)
    print(f"Output:\n"
          f"{txt}")
    exit()

if len(argv) != 3:
    exit("Invalid usage")

if argv[1] not in ["--font", "-f"]:
    exit("Invalid usage")

if argv[2] not in lists:
    exit("Invalid usage")

figlet.setFont(font=argv[2])
text = input("Input: ")
txt = figlet.renderText(text)
print(f"Output:\n"
      f"{txt}")