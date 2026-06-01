
limits = {
    "temperature": (20, 80),
    "pressure": (30, 100),
    "voltage": (210, 240)
}

while True:
    choice = input("choose sensor: ").strip().lower()
    if choice not in limits:
        print("Invalied choise try again.")
        continue
    break
    
low_limit, high_limit = limits[choice]        

while True:
    data = input(": ")
    if data == "done":
        break
    
    try:
        data = float(data)
    except ValueError:
        continue

    if data > high_limit:
        print("High")

    elif data < low_limit:
        print('Low')

    else:
        print("Normal")
