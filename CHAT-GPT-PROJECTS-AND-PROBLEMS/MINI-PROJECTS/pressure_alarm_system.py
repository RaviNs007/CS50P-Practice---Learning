def main():
    
    Pressures = []
    High_alarm = 0
    Low_alarm = 0
    
    while True:
        Pressure = (input("Enter Pressure: ").strip().lower())
                  
        if Pressure.isdigit():
            
            Pressure = float(Pressure)
            Pressures.append(Pressure)
            
            if Pressure > 100:
                print("High Pressure")
                
                High_alarm += 1
                
            elif Pressure < 20:
                print("Low Pressure")
                
                Low_alarm += 1
                
            else:
                print("Normal")
            
        elif Pressure == "done":
                
            print(f' Max pressure = {max(Pressures)} ')
            print(f' Min pressure = {min(Pressures)} ')
            print (f' Average pressure = {sum(Pressures)/len(Pressures)}')
            print(f' Total alarms triggered = {High_alarm + Low_alarm}')
            print(f' Total High Alarm = {High_alarm}')
            print(f' Total Low Alarm = {Low_alarm}')
            
            break
                       

main()