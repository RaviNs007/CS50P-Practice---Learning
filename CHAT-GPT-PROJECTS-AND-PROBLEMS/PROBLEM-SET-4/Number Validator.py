while True:
    num =  input(": ")
    
    try:
        num = int(num)
        
    except ValueError:
        continue
        
    if not 1 <= num <= 100:
        continue
    break

print(f"Accepted: {num}")