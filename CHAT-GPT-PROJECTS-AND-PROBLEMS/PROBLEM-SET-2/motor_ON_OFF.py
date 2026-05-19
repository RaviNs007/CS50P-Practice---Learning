def main():
    status = input("Is motor running?: ").strip().lower()
    
    print(s_checker(status))


def s_checker(status):
    
    if status == "yes" or status == "y" or status == "running":
        return "MOTOR ON"

    return "MOTOR OFF"
    
main()