def main():
    mass = int(input("Enter the mass: "))
    energy = mass*300000000*300000000
    print("Energy equivalent to", mass,"KG mass = ", f"{energy:,}", "Joules")
    print("in tera joules", energy/1000000000000, "TJ")

main()
