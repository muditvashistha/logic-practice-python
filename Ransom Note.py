# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

ransomNote="ransom"
magazine="random"
x=[]
y=[]
for i in magazine:
    x.append(i)
    
for i in ransomNote:
    y.append(i)

counter=0
for j in y:
    if j in x:
        x.remove(j)
        counter+=1
if counter==len(ransomNote):
    print(True)
else:
    print(False)
