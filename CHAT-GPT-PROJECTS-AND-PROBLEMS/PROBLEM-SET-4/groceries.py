def main():
    grocery_list = {}

    while True:
        try:
            item = input(": ").strip().upper()
        except EOFError:
            break     
            
        if item.isdecimal() or  item == "":
            continue
       
        grocery_list[item] = grocery_list.get(item, 0)+1

    for item in sorted(grocery_list):
        
        print(f"{grocery_list[item]} {item}")
        
    
main()