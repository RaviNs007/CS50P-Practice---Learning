def main():
    exp = input("Expression: ")

    print(calc(exp))


def calc(exp):

    x, y, z = exp.split(" ")

    a = int(x)

    b = int(z)

    if y == '+':
        return float(a+b)

    elif y == '-':
        return float(a-b)

    elif y == "*":
        return float(a*b)

    elif y == "/":
        if b == 0:
            return "Can't divide by zero"
        else:
            div = (a/b)
            return round(div, 1)

main()