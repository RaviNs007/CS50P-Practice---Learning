def main():
    
    UP_Level = float(input("Enter fuel density at upper level of storage tank: ").strip())
    MID_Level = float(input("Enter fuel density at middle level of storage tank: ").strip())
    LOW_Level = float(input("Enter fuel density at lower level of storage tank: ").strip())
    
    
    avg = round(((UP_Level + LOW_Level + MID_Level)/3),2)
    print("Average density = " + str(avg))
    
    if 0.79 <= avg <= 0.84:
        print("PASS")
        
    else:
        print("FAIL")
    
main()