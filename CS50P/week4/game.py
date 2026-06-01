import random

while True:
    level = input("Level: ")
    if not level.isdigit():
        continue

    level = int(level)

    if not 0 < level:
        continue
    break
num = random.randint(1, level)

#count = 0
while True:
    guess = input("Guess: ")

    if not guess.isdigit():
        continue

    guess = int(guess)

    #count += 1

    if guess == num:
        print("Just right!")

        #print("You took", count, "guesses")

        break

    elif guess > num:
        print("Too large!")

    else:
        print("Too small!")