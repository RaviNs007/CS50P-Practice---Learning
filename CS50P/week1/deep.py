def main():

    qus = input("What is the answer to the Great Question of Life, the Universe and Everything?____: ")

    print(think(qus))

def think(ans):
    ans = ans.lower().strip()
    
    if ans == "42":
        return "Yes"
        
    elif ans == "forty two":
        return "Yes"
        
    elif ans == "forty-two":
        return "Yes"

    return "No"

"""
def think(ans):
    ans = ans.lower().strip()
    
    if ans == "42" or ans == "forty two" or ans == "forty-two"
        return "Yes"

    return "No"
"""

main()