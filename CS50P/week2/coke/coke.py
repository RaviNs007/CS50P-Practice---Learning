def main():
    amount_due = 50
    aceptable_curreny = [25, 5, 10]
    while True:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        
        if coin in aceptable_curreny:
            amount_due = amount_due - coin
            
        else:
            continue
        
        if amount_due <= 0:
            print( f"Coin Owed: {abs(amount_due)}")
            break
main()