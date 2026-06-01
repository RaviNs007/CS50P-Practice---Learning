import json


def main():
    with open("Traffic_lights.json", "r") as file:
        data = json.load(file)

    if not data["last"] or data["last"] == "green":
        print(data["stop"],"❤️")
        data["last"] = "red"

    elif data["last"] == "red":
        print(data["pause"],"💛")
        data["last"] = "yellow"

    else:
        print(data["go"],"💚")
        data["last"] = "green"

    with open("Traffic_lights.json", "w") as file:
        json.dump(data, file, indent=4)

main()