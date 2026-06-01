stock = {}

while True:
    
    item = input(": ").strp().upper()
    
    if item == "DONE":
        break
    
    stock[item] = stock.get(item, 0) + 1
    
for item in sorted(stock):    
    print(f"{item}: {stock[item]}")
    

