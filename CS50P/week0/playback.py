s = input("text: ")
#print(s.replace(' ', '...'))




vowl = 'aeiouAEIOU'
for char in s:
    if char in vowl:
        s = s.replace(char, '')
print(s)



