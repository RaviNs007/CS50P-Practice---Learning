def main():
    string = input("camelCase: ").strip()
    
    
    print(f"snake_case: {camel_to_snake_case(string)}")
    

def camel_to_snake_case(string):
    
        for c in string:
            
            if c.isupper():
                string = string.replace(c, "_"+c)
            
        string = string.lower()
        return string

main()