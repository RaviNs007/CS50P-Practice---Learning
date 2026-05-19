def main():
    level = float(input("Enter the water level in(%): " ).strip())
    
    print(W_level_checker(level))
    
    
def W_level_checker(level):
    if 0 <= level <= 20:
        return "LOW LEVEL"
        
    elif 20 < level <=80:
        return "STABLE"
    
    elif 80 < level <= 100:
        return "FULL"
        
    return "INVALID LEVEL"
    
main()