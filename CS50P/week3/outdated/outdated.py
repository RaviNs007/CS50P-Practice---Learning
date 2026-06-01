def main():
    months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" :4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
    }
    while True:
        date = input("Date: ").strip()

        try:
            (month, day, year) = date.split("/")

            day = int(day)
            month = int(month)
            if not 1 <= day <= 31 or not  1<= month <= 12:
                continue
            break

        except ValueError:
            try:
                (month, day, year) = date.split(" ")
                month = month.strip().capitalize()

                if month not in months:
                    continue

                if not day.endswith(","):
                    continue

                day = day.strip(",")
                day = int(day)

                if not  1 <= day <= 31:
                    continue

                month = months[month]
                break

            except ValueError:
                continue

    print(f"{year}-{month:02}-{day:02}")

main()

