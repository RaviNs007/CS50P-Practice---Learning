def main():
    
    text =  input("Input: ")
    
    print(f"Output: {vowel_rm(text)}")
    
def vowel_rm(text):
    vowels =  "AEIOUaeiou"
    
    for char in text:
        if char in vowels:
            text = text.replace(char, "")
        
    return text
    
main()