import json


def main():
    while True:

        with open("power_latch.json", "r") as file:
            data = json.load(file)

            start = data["start_button"]
            stop = data["stop_button"]
            motor = data["motor"]

        if not motor:
            print("Motor OFF")
        elif motor:
            print("Motor ON")

        command = input("Type the button to press: ").strip().lower()

        if command == "end":
            break

        elif command == "start" and not motor and not stop and not start:
            data["start_button"] = True
            data["motor"]  = True

        elif command == "start" and motor and start:
            data["start_button"] = False

        elif command == "start" and motor and not start:
            data["start_button"] = True

        elif command == 'stop' and motor:
            data["motor"] = False
            data["stop_button"] = True
            data["start_button"] = False

        elif command == 'stop' and not motor and stop:
            data["stop_button"] = False


        with open("power_latch.json", "w") as file:
            json.dump(data, file, indent=4)


if __name__ == '__main__':
    main()