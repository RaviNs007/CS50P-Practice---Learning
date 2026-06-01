def main():
    grocery_list = {}
    
    while True:
        try:
            item = input(": ").strip().upper()
        except EOFError:
            break    
        
        grocery_list[item] = grocery_list.get(item, 0) + 1              #count = 1                                   # 
                                                                        #if item in grocery_list:
    for items in sorted(grocery_list):                                      #count += grocery_list.get(item)
        print(grocery_list[items], items)                                   #grocery_list.update({item : count})
        
main()