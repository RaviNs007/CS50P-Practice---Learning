def main():
    
    Temperatures = []
    High_alerts = 0
    Low_alerts = 0
    
    while True:

        Temperature = (input("Enter Temperature: ").strip().lower())

        if Temperature == "done" and Temperatures:
            print(f' Total Readings: {len(Temperatures)}')
            print(f' Highest Temperature: {max(Temperatures)} ')
            print(f' Lowest Temperature: {min(Temperatures)} ')
            print(f' Average Temperature: {sum(Temperatures)/len(Temperatures)}')
            print(f' Total Alerts triggered: {High_alerts + Low_alerts}')
            print(f' Total High Alerts: {High_alerts}')
            print(f' Total Low Alerts: {Low_alerts}')

            break
        elif Temperature == "done" and not Temperatures:
            print('No data collected')
            break
            
        try:
            Temperature = float(Temperature)
            
            Temperatures.append(Temperature)
            
            if Temperature > 80:
                print("High Temperature")
                
                High_alerts += 1
                
            elif Temperature < 20:
                print("Low Temperature")
                
                Low_alerts += 1
                
            else:
                print("Normal")
           
        except ValueError:
            print("Please enter a correct value")
            continue
                            

main()