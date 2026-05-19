def main():
    pressure = ""
    while True:
        pressure = (input("Enter pressure: ").strip().lower())
        
        if pressure == "exit":
            break
            
        else:
            pressure = float(pressure)
            
            if pressure > 100:
                print("WARNING!!!")
        

main()
    