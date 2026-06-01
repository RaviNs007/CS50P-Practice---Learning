def main():
    while True:
        
        try:
            day, month, year = date_parse(input(": ").strip().capitalize())
            day = int(day)
            month = int(month)
        except (ValueError, TypeError):
            continue
        
        if not 1 <= day <= 31:
            continue
        if not 1 <= month <= 12:
            continue
            
        print(f"{year}-{month:02}-{day:02}")
        break

def date_parse(date):
    months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }
    if date == "":
        return
    if "/" in date:
        month, day, year = date.split("/")

    else:
        month, day, year = date.split(" ")
        
        if day.endswith(","):
            day = day.strip(",")
        
        if month in months:
            month = months[month]
        
    return day, month, year    
    
main()