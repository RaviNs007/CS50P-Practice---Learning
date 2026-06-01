import requests
from sys import argv, exit


def main():
    if len(argv) != 2:
        exit("Missing command-line argument")

    try:
        argv[1] = float(argv[1])
    except ValueError:
        exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=335536caeb254b626d291b57c60be3f0684c109862972ab2f4c3eb67f95995ad"
        )
        response.raise_for_status()
    except requests.RequestException:
        exit("There is a problem with server please try again later")

    content = response.json()
    price = float(content["data"]["priceUsd"])
    amount = price * argv[1]
    print(f"${amount:,.4f}")


main()
