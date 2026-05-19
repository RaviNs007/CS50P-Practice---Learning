def main():
    plate = input("Plate: ").strip().upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    start_num = False

    if not s.isalnum():
        return False

    if not 2 <= (len(s)) <= 6:
        return False

    if not s[:2].isalpha():
        return False

    for num in s[2:]:

        if num.isdecimal():
            if num == '0' and not start_num:
                return False

            start_num = True

        if num.isalpha() and start_num:
            return False

    return True


main()
