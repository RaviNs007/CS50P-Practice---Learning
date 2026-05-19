while True:
    s = ""
    save = ''
    numbs = False
    chums = ''
    s = input(": ").strip().upper()
    if s.isalnum():
        
        if 2 <= (len(s)) <= 6:
            
            if s[:2].isalpha():
                
                for num in s[2:]:
                    
                    if num.isdecimal():
                        save += num
                        
                    chums += num
                    

                        
                        
                if save[:1] != '0' and chums.isdecimal:
                    
                    print("Holla",s,chums)
       
