import json

def main():

    with open("dual_tank.json", "r") as file:
        data = json.load(file)

    if data["tank_a"] < 10:
        data["transfer_pump"] = False
        data["low_supply_alarm"] = True

    elif data["tank_a"] > 10:
        data["low_supply_alarm"] = False


    if data["tank_b"] > 85:
        data["transfer_pump"] = False

    elif data["tank_b"] < 20 and data["tank_a"] > 10:
        data["transfer_pump"] = True


    if data["transfer_pump"]:
        data["tank_a"] -= 5
        data["tank_b"] += 5

    if data["tank_b"] > 5:
        data["tank_b"] -= 2


    print("Tank A           :" ,data["tank_a"])
    print("Tank B           :" ,data["tank_b"])
    print("Transfer pump    :", data["transfer_pump"])
    print("Low supply alarm :", data["low_supply_alarm"])

    with open("dual_tank.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    main()