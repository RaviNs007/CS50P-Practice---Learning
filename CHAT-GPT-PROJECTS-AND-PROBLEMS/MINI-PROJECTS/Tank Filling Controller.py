tank_level = 0
while True: 
    command = input('> ').strip().lower()
    if command == 'exit':
        break
    elif command == 'status':
        print(f'Tank Level: {tank_level}%')
        
        
    if command == "fill":
        if tank_level < 100:
            tank_level += 10
            print(f'Tank Level: {tank_level}%')
            
        else:
            print('Tank already full')
            
        
    elif command == "drain":
        if tank_level > 0:
            tank_level -= 10
            print(f'Tank Level: {tank_level}%')
        
        else:
            print('Tank already empty')