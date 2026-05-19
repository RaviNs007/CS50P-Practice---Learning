def main():
    
    password = input("Enter Password: ")
        
    if password_check(password):
        print(f"{password} is Vaild")
        
    else:
        print(f"{password} is Invalid")
    

def password_check(password):
    
    if len(password) < 8:
        return False
        
    if password.isalnum():
        
        if password.isalpha():
            return False
        
        elif password.isdigit():
            return False
        
        else:
            return True
        
    else:
        return False
main()

# use has_number
# has_letter