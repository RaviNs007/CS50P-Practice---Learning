def main():
    
    readings, invalid_count = process_data()
    print_report(readings, invalid_count)
    
def process_data():
    readings = []
    invalid_count = 0
    while True:
        
        reading = input(": ").strip().lower()
        
        if  reading == "done":
            break
        
        if not reading:
            invalid_count += 1
            continue
            
        try:
            reading = float(reading)
            
        except ValueError:
            invalid_count += 1
            continue
        
        if not 0 <= reading <= 1000:
            invalid_count += 1
            continue
            
        readings.append(reading)
        
    return readings, invalid_count

def print_report(readings, invalid_count):
    
    if not readings:
        print("No valid readings")
        return
    
    average = round(sum(readings)/len(readings), 2)


    if average < 100:
        status = 'LOW AVERAGE'
    elif 100 <= average <= 700:
        status = 'NORMAL'
    else:
        average > 700
        status = 'HIGH AVERAGE'

    print(f"""
    ========================================
    #                Report                #
    ========================================
    Total Valid Readings   : {len(readings)}
    Invalid readings       : {invalid_count}
    Highest Reading        : {max(readings)}
    Lowest Reading         : {min(readings)}
    Average Reading        : {average}
    Status                 : {status}

    """)
    
main()