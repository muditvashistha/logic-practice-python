x="ABC $. def01ASDF.."
y=str.lower(x)
y=y.replace(" ","")
print(y)

special_characters=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
 ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', 
 '}', '~']

for i in y:
    if i in special_characters:
        y=y.replace(i,"")

print(y)

if y==y[::-1]:
    print("Palindrome")
else:
    print("No Palindrome")
