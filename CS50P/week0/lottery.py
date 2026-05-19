import random 
def lottery(num):
    match num:
        case 1:
            return "Good Luck For Next Time"
        case 2:
            return "Better Luck Next Time"
        case 3:
            return 'You Got a Second Try'
        case 4:
            return 'You Won A Candy'
        case 5:
            return "You Won A Matchbox"
        case 6:
            return "You Won Nothing"
        case 7:
            return "Congratulations You Won The Lottery"
        case 8:
            return "Better Luck Next Time"
        case 9:
            return "You Got 2 More Chances"


print(lottery(random.randint(1,9)))