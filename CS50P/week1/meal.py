def main():

    time = input("What time is it?: ")
    n_time = convert(time)

    if 7 <= n_time <= 8:
        print("breakfast time")

    elif 12 <= n_time <= 13:
        print("lunch time")

    elif 18 <= n_time <= 19:
        print("Dinner time")
    
    
    print(convert(time))


def convert(time):
    hour, mint = time.split(":")

    h = float(hour)
    m = float(mint)

    return h + (m/60)


if __name__ == "__main__":
    main()

