fruits = {}
while True:
    fruit = input(": ").strip().upper()
    if fruit == "DONE":
        break
    fruits[fruit] = fruits.get(fruit, 0)+1
    
for fruit in sorted(fruits):
    print(f"{fruit}: {fruits[fruit]}")