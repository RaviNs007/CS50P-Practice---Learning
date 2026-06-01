import inflect
import sys

p = inflect.engine()

name_list = []
while True:
    try:
        name = input("Name: ")

        name_list.append(name)
    except EOFError:
        break
if not name_list:
    sys.exit()
print(f" Adieu, adieu, to {p.join(name_list)}")


