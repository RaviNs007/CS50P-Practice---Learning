import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        num1, num2 = generate_integer(level)

        for _ in range(3):
            try:
                ans = int(input(f"{num1} + {num2} = "))
            except ValueError:
                print("EEE")
                continue

            if ans == num1+num2:
                score += 1
                break
            print("EEE")
        else:
            print(f"{num1} + {num2} = {num1+num2}")

    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if not level.isdigit():
            continue
        level = int(level)
        if not 0 < level <= 3:
            continue
        return level


def generate_integer(level):
    if level == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        return num1, num2

    elif level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        return num1, num2

    else:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
        return num1, num2



if __name__ == "__main__":
    main()