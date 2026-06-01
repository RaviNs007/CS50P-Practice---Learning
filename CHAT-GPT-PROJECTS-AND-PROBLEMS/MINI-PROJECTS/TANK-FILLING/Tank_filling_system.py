import json


def main():
    with open("Tank_filling_record.json", "r") as file:
        data = json.load(file)

    if data["tank_level"] < 90:
        while True:
            command = input("Type the button to press: ").strip().lower()

            if command not in ["start", "stop", "continue", "c"]:
                print('Please enter correct command')
                continue

            elif command == "c" or command == "continue":
                break

            elif command == "start" and not data["pump"]:
                data["start_button"] = True
                data["pump"] = True
                data["start_button"] = False
                break

            elif command == 'stop' and data["pump"]:
                data["stop_button"] = True
                data["pump"] = False
                data["stop_button"] = False
                break

    data["tank_level"] -= 2

    if data["tank_level"] <= 20:
        data["pump"] = True

    if data["pump"]:
        if data["tank_level"] > 85:
            data["tank_level"] += 90-data["tank_level"]
            data["pump"] = False

        else:
            data["tank_level"] += 5

    print(f"""
                START BUTTON : {data["start_button"]}
                STOP BUTTON  : {data["stop_button"]}
                PUMP         : {data["pump"]}
                TANK LEVEL   : {data["tank_level"]}
                

        """)

    with open("Tank_filling_record.json", "w") as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    main()
