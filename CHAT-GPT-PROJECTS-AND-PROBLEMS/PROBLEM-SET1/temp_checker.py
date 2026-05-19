def main():
    temperature = float(input("Enter The Temperature: ").strip())
    
    print(checker(temperature))
    
def checker(temperature):
    if temperature < 20:
        return "LOW TEMPERATURE"
        
    elif 20 <= temperature <= 80:
        return "NORMAL"
        
    return "HIGH TEMPERATURE"
    
if __name__ == "__main__":
    main()