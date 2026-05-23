def main():
    Machine_Status_ON = False    
    while True:
        
        state = input("Command: ").strip().upper()
        
        if state == "EXIT"
            break
        
        if state not in ["START", "STATUS", "STOP"]:
            continue
        
        if Machine_Status_ON:
            
            if state == 'STATUS':
                print("Machine is ON")
             
            elif state == 'START':
                print("Machine already started")
                    
            elif state == 'STOP':
                print("Machine stopped")
                Machine_Status_ON = False
        
        elif not Machine_Status_ON:
            
            if state == 'STATUS':
                print("Machine is OFF")
            
            elif state == 'STOP':
                print("Machine already stopped")
            
            elif state == 'START':
                print("Machine started")  
                Machine_Status_ON = True

main()
