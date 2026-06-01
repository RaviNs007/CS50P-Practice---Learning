def main():

    while True:
        
        fraction = input("Fraction: ")
        try:    
            (x, y)  = fraction.split('/')
            x = int(x)
            y = int(y)
            if x > y:
                raise ValueError
            percentage = round((x/y)*100)
            break
        except (ValueError, ZeroDivisionError):
            continue
        
    if percentage <= 1:
        print("E")
        
    elif 1 < percentage < 99:
        print(f"{percentage}%")
        
    else:
        print('F')
        
main()