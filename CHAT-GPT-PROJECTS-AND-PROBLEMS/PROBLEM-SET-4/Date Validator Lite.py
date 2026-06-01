def main():
    while True:
        date = input(": ").strip()
        try:
            day, month, year = date.split("/")
            day = int(day)
            month = int(month)
            year = int(year)
            
        except ValueError:
            continue
            
        if not 1 <= day <= 31 or not 1 <= month <= 12 or not 1900 <= year <= 2100:
            continue
            
        break    
    print(f"Valid date: {day:02}-{month:02}-{year}")
  
main()