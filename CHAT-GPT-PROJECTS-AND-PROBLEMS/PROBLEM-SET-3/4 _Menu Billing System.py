menu = {
    "tea": 10,
    "coffee": 20,
    "samosa": 15
}
total = 0
while True:
    order = input(": ").strip().lower()
    if order == "done":
        break
    elif order in menu:
        total += menu[order]
        print(f" Total: ₹{total}")
    else:
        continue