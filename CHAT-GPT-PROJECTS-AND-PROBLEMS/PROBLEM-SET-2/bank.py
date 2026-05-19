def main():
    reply = input("Greetings: ")
    print(hello_checker(reply))

def hello_checker(greet):
    greet = greet.strip().lower()
    if greet.startswith("hello"):
        return "$0"

    elif greet.startswith("h"):
        return "$20"

    return "$100"

main()