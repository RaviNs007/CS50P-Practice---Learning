def main():
    
    name = input("Name: ").strip().upper()
        
    if name_check(name):
        print(f"{name} is Vaild")
        
    else:
        print(f"{name} is Invalid")
    

def name_check(name):
    
    if not name[:3].isalpha():
        return False
    
    if not 3 <= len(name) <= 8:
        return False
        
    if not name.isalnum():
        return False
    
    num_start = False
    
    for char in name[3:]:
        
        if char.isdigit():
            
            if char == "0" and not num_start:
                return False
                
            num_start = True
            
            
        if char.isalpha() and num_start:
            return False
            
    return True
    
main()
