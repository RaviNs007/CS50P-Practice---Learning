attempt = 3
while True:
    
    if attempt == 0:
        print("Account locked")
        break
    password = input("Password:")
    
    if password == "":
        print("Password cannot be empty")
        continue
    
    if password == "python123":
        print("Access granted")
        break
        
    else:
        attempt -= 1
        print(f"Wrong password. Attempts left: {attempt}")